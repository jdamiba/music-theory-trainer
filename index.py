import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from questions import questions

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    [
        html.H4("Music Theory Quiz"),
        # dcc.Store(id="memory"),
        html.Div(
            id="instructioins-div",
            children='Note names are [A, B, C, D, E, F, G] \nUse "#" (shift + 3) for sharps and "b" (lowercase b) for flats. \n For questions about intervals, use one of [m2, M2, m3, M3, P4, TT, P5, m6, M6, m7, M7]\n For questions about chord tonality, use one of [minor, major, diminished]\n',
            style={"whiteSpace": "pre-line"},
        ),
        html.Br(),
        html.Div(id="question-div", children=questions[0][0]),
        dcc.Input(id="answer-input", type="text", value=""),
        html.Button(id="button", children="Submit"),
        html.Br(),
        html.Br(),
        html.Div(id="output", style={"whiteSpace": "pre-line"}),
    ]
)

@app.callback(
    Output('question-div', 'children'),
    Output('output', 'children'),
    Input('button', 'n_clicks'),
    Input('answer-input', 'value')
)
def generate_question(n_clicks, user_answer):
    if n_clicks is None:
        return dash.no_update, dash.no_update

    return questions[n_clicks][0], "Correct!" if user_answer == questions[n_clicks - 1][1] else "incorrect! The correct answer to {} is {}".format(questions[n_clicks - 1][0], questions[n_clicks - 1][1])

if __name__ == '__main__':
    app.run_server(debug=True)