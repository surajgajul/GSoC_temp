from django.shortcuts import render, HttpResponse
from myapp.models import Sales
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from rest_framework import generics
from .models import Sales
from .serializers import SalesSerializer

# Create your views here.
class SalesListAPIView(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

def home(request):
    return render(request, 'home.html')
# def home(request):
#     qs=Sales.objects.all()
#     sales_data=[
#         {
#             'Invoice ID':x.invoice_id,
#             'Branch':x.branch,
#             'City':x.city,
#             'Customer type':x.customer_type,
#             'Gender':x.gender,
#             'Product line':x.product_line,
#             'Unit price':x.unit_price,
#             'Quantity':x.quantity,
#             'Tax 5%':x.tax,
#             'Total':x.total,
#             'Date':x.date,
#             'Time':x.time,
#             'Payment':x.payment,
#             'cogs':x.cogs,
#             'gross margin percentage':x.gross_margin_percentage,
#             'gross income':x.gross_income,
#             'Rating':x.rating
#         } for x in qs
#     ]
#     df=pd.DataFrame(sales_data)
#     city_counts=df['City'].value_counts()
#     counts=df['Payment'].value_counts()
#     counts_prod = df['Product line'].value_counts().reset_index()
#     counts_prod.columns = ['Product line', 'Count']
#     # Create a new column to categorize time as 'Before Noon' or 'After Noon'
#     df['Time_Category'] = df['Time'].apply(lambda x: 'Before Noon' if x.hour < 12 else 'After Noon')
#     # Group by 'City' and 'Time_Category', then calculate the sum of rows for each group
#     sum_by_time_category = df.groupby(['City', 'Time_Category']).size().reset_index(name='Total Samples')
#     fig=px.pie(names=city_counts.index, values=city_counts.values, title='Citywise Distribution', hole=0.6)
#     fig1=px.histogram(df, x='Rating', nbins=10, title='Ratings Distribution')
#     fig2=px.pie(names=counts.index, values=counts.values, title='Payment Method Distribution')
#     fig3=px.scatter(df, y='gross income', title='Income Chart')
#     fig4=px.bar(counts_prod, x='Product line', y='Count', title='Product based distribution')
#     fig5=px.line(df, y='Total', title='Margin Chart')
#     fig6=px.bar(df, x='City', color='Payment', title='Payment Method Distribution by City', barmode='group')
#     fig7=px.bar(sum_by_time_category, x='City', y='Total Samples', color='Time_Category', title='Samples Distribution by Time of Day in Each City', barmode='group')
#     gantt_plot = plot(fig, output_type="div")
#     gantt_plot1 = plot(fig1, output_type="div")
#     gantt_plot2 = plot(fig2, output_type="div")
#     gantt_plot3 = plot(fig3, output_type="div")
#     gantt_plot4 = plot(fig4, output_type="div")
#     gantt_plot5 = plot(fig5, output_type="div")
#     gantt_plot6 = plot(fig6, output_type="div")
#     gantt_plot7 = plot(fig7, output_type="div")
#     context = {'plot_div': gantt_plot, 'plot_div1': gantt_plot1, 'plot_div2': gantt_plot2, 'plot_div3': gantt_plot3, 'plot_div4': gantt_plot4, 'plot_div5': gantt_plot5, 'plot_div6': gantt_plot6, 'plot_div7': gantt_plot7}
#     return render(request, "home.html", context)