
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import string
import os

app = Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


master_folder = '/Users/kurniawankesumaputra/Desktop/work/dkatalis/technical_test/'
file_path = os.path.join(master_folder,*['data','LuxuryLoanPortfolio.csv'])
df = pd.read_csv(file_path)
df.columns = df.columns.str.translate(str.maketrans('', '', string.punctuation)).str.replace(' ','_').str.lower().str.strip()
df['fundeddate'] = pd.to_datetime(df['fundeddate'])
df['funded_date_year'] = df['fundeddate'] + pd.offsets.MonthBegin(-1)

#total loan and average funded per purpose loan
purpose_loan = df.groupby(['purpose'],as_index=False).agg({
    'loanid':lambda x:x.nunique(),
    'fundedamount':lambda x:x.median()
})
purpose_fig = make_subplots(specs=[[{"secondary_y": True}]])
purpose_fig.add_trace(
    go.Bar(
        x=purpose_loan['purpose'],
        y=purpose_loan['loanid'],
        name = "number of loan"
    ),
    secondary_y=False
)
purpose_fig.add_trace(
    go.Scatter(
        x=purpose_loan['purpose'],
        y=purpose_loan['fundedamount'],
        name = "avg funded amount"
    ),
    secondary_y=True
)
purpose_fig.update_layout(
    title_text="Number of Loan and Average of Funded Amount per Purpose Loan"
)
purpose_fig.update_yaxes(title_text="Number of Loan",secondary_y=False)
purpose_fig.update_yaxes(title_text="Average Funded Amount",secondary_y=True)

#interest rate per purpose loan
interest_rate_purpose = go.Figure()
for purpose in df['purpose'].unique():
    interest_rate_purpose.add_trace(
        go.Box(
            x=df[df["purpose"]==purpose]['interest_rate_percent'],
            name=purpose
        )
    )


interest_rate_purpose.update_layout(
    title_text="Interest Rate per Purpose Loan"
)
interest_rate_purpose.update_xaxes(title_text="Interest Rate")
interest_rate_purpose.update_yaxes(title_text="Purpose")

#Funded Amount per time
funded_amount_time = df.groupby(['funded_date_year'],as_index=False).agg(
    {
        'loanid':lambda x:x.nunique(),
        'fundedamount':lambda x:x.sum()
    }
).sort_values(['funded_date_year'],ascending=True)

funded_amount_time_fig = make_subplots(specs=[[{"secondary_y": True}]])
funded_amount_time_fig.add_trace(
    go.Scatter(
        x=funded_amount_time['funded_date_year'],
        y=funded_amount_time['fundedamount'],
        name='funded amount'
    ),
    secondary_y=True
)
funded_amount_time_fig.add_trace(
    go.Scatter(
        x=funded_amount_time['funded_date_year'],
        y=funded_amount_time['loanid'],
        name = 'number of loan'

    ),
    secondary_y=False
)

funded_amount_time_fig.update_layout(
    title_text="Number of Loan and Funded Amount per Month"
)
funded_amount_time_fig.update_xaxes(title_text="Month")
funded_amount_time_fig.update_yaxes(title_text="Number of Loan",secondary_y=False)
funded_amount_time_fig.update_yaxes(title_text="Funded Amount",secondary_y=True)



app.layout = html.Div(children=[
    html.H1(
        children='Luxury Loan Portfolio',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='purpose_loan',
        figure=purpose_fig
    ),
    dcc.Graph(
        id='property_value',
        figure=interest_rate_purpose
    ),
    dcc.Graph(
        id='funded_amount_time',
        figure=funded_amount_time_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
