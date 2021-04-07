import pandas as pd
import plotly.express as px
import streamlit as st


def relative_bar_chart(columna_total=None, columna_unica=None, pivot=None,
					   ejex=None, color=None, fila=None, columna=None, indices=None):
	if columna_total == "Total":
		total = pivot[columna_unica].sum()
		pivot['Frecuencia'] = pivot[columna_unica] / total
	else:
		total = pivot.pivot_table(index=columna_total,
								values=columna_unica,
				 				aggfunc='sum').rename(columns={columna_unica:"TOTAL"}).reset_index()

		pivot = pivot.merge(total, on=columna_total)
		pivot['Frecuencia'] = pivot[columna_unica] / pivot["TOTAL"]

	fig = px.bar(pivot, x=ejex,
				 y="Frecuencia", color=color,
				 facet_row=fila, facet_col=columna, barmode="group",
				 color_discrete_sequence=px.colors.qualitative.Pastel,
				 color_continuous_scale=px.colors.sequential.GnBu,
				 text="Frecuencia",
				 facet_col_wrap=4)

	fig.for_each_yaxis(lambda yaxis:  yaxis.update(tickformat = ',.0%'))
	fig.update_traces(textposition='outside', texttemplate='%{text:,.2%}')
	return fig

def absolute_bar_chart(columna_unica=None, pivot=None, ejex=None, color=None, fila=None, columna=None, category_orders=None):
	fig = px.bar(pivot, x=ejex, y=columna_unica,
		   color=color, facet_row=fila,
		   facet_col=columna, barmode="group",
		   color_discrete_sequence=px.colors.qualitative.Pastel,
		   color_continuous_scale=px.colors.sequential.GnBu,
		   text=columna_unica,
		   facet_col_wrap=4,
		   category_orders=category_orders)
	fig.update_traces(textposition='outside', texttemplate='%{text}')
	fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
					  template = "simple_white")
	return fig


def bar_chart(columna_unica=None, pivot=None, ejex=None, color=None, fila=None, columna=None, indices=None, category_orders=None):
	st.write(columna_unica)
	if st.checkbox("Visualizar frecuencia relativa"):
		columna_total = st.selectbox("Relativo respecto a: ", ["Total"]+indices)
		fig = relative_bar_chart(columna_total=columna_total,
								 columna_unica=columna_unica,
								 pivot=pivot, ejex=ejex, color=color,
								 fila=fila, columna=columna, indices=indices, category_orders=category_orders)
	else:
		fig = absolute_bar_chart(columna_unica=columna_unica,
								 pivot=pivot, ejex=ejex, color=color,
								 fila=fila, columna=columna, category_orders=category_orders)
	return fig

def box_chart(columna_unica=None, pivot=None, ejex=None, color=None, fila=None, columna=None, indices=None):
	fig = px.box(pivot, x=ejex, y=columna_unica,
		   color=color, facet_row=fila,
		   facet_col=columna,
		   color_discrete_sequence=px.colors.qualitative.Pastel,
		   facet_col_wrap=4)
	return fig


def scatter_chart(columna_unica=None, pivot=None, ejex=None, color=None, fila=None, columna=None, lista_agrupadores=None, category_orders=None):
	ejey = st.selectbox("Elija eje Y: ", lista_agrupadores)
	fig = px.scatter(pivot, x=ejex, y=ejey,
		   color=color, facet_row=fila,
		   facet_col=columna,
		   color_discrete_sequence=px.colors.qualitative.Pastel,
		   color_continuous_scale=px.colors.sequential.GnBu,
		   facet_col_wrap=4,
		   category_orders=category_orders)
	return fig

def categories_order(answers):
	satisfaction = ["Nada satisfecho", "Un poco satisfecho", "Neutra", "Muy satisfecho", "Totalmente satisfecho", "No puedo asistir"]
    yes_no = ["Sí", "No"]
    if len(set(satisfaction) - answers) < 2:
    	cat_order = satisfaction
    elif len(set(yes_no) - answers) < 2:
    	cat_order = yes_no
    else:
    	cat_order = list(answers)        
	return {pregunta: cat_order, "GENERO": ["F", "M"]}
