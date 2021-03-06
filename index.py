import dash
import dash_core_components as dcc
import dash_html_components as html
import random

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from questions import questions

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

random.shuffle(questions)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    [
        html.H4(id="header", children="Music Theory Quiz"),
        dcc.Store(id="local", storage_type="local"),
        html.Div(
            id="instructioins-div",
            children='Note names are [A, B, C, D, E, F, G] \nUse "#" (shift + 3) for sharps and "b" (lowercase b) for flats. \n For questions about intervals, use one of [m2, M2, m3, M3, P4, TT, P5, m6, M6, m7, M7]\n For questions about chord tonality, use one of [minor, major, diminished]\n',
            style={"whiteSpace": "pre-line"},
        ),
        html.Br(),
        html.Div(id="question-div"),
        dcc.Input(id="answer-input", type="text", value=""),
        html.Button(id="button", n_clicks=0, children="Submit"),
        html.Br(),
        html.Br(),
        html.Div(id="output", style={"whiteSpace": "pre-line"}),
    ]
)


@app.callback(Output("local", "data"), Input("header", "children"), prevent_initial_call=True)
def load_questions(self):
    return questions


@app.callback(
    Output("question-div", "children"),
    Output("output", "children"),
    Output("answer-input", "value"),
    Input("button", "n_clicks"),
    State("answer-input", "value"),
    State("local", "data"),
)
def generate_question(n_clicks, user_answer, data):
    print(data[:4])
    print("n_clicks is {}".format(n_clicks))
    if n_clicks == 0:
        return data[0][0], dash.no_update, ""

    next_question = data[n_clicks][0]
    previous_question = data[n_clicks - 1][0]
    previous_answer = data[n_clicks - 1][1]

    print("next question is {}".format(next_question))
    print("previous question is {}".format(previous_question))
    print("previous answer is {}".format(previous_answer))

    if user_answer == previous_answer:
        return (
            next_question,
            'Correct!\n {} is the correct answer to the question: "{}"'.format(
                user_answer, previous_question
            ),
            "",
        )
    else:
        return (
            next_question,
            'Incorrect! {} is the correct answer to the question: "{}".\n You answered {}.'.format(
                previous_answer, previous_question, user_answer
            ),
            "",
        )


if __name__ == "__main__":
    app.run_server(debug=True)
