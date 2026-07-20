import math
import re
import streamlit as st


# Set the browser tab title and page layout
st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)


# Create starting values
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "answer" not in st.session_state:
    st.session_state.answer = "0"


# Add a number or symbol to the input
def add_value(value):
    st.session_state.expression += value


# Clear the calculator
def clear_input():
    st.session_state.expression = ""
    st.session_state.answer = "0"


# Remove the last entered character
def remove_last_character():
    st.session_state.expression = st.session_state.expression[:-1]


# Convert a number into percentage
def calculate_percentage():
    try:
        number = float(st.session_state.expression)
        result = number / 100

        # Remove .0 from whole number results
        if result.is_integer():
            result = int(result)

        # Show result in the same input box
        st.session_state.expression = str(result)
        st.session_state.answer = str(result)

    except ValueError:
        st.session_state.expression = "Error"


# Calculate sine using degrees
def sin_degree(number):
    return math.sin(math.radians(number))


# Calculate cosine using degrees
def cos_degree(number):
    return math.cos(math.radians(number))


# Calculate tangent using degrees
def tan_degree(number):
    return math.tan(math.radians(number))


# Calculate the entered mathematical expression
def calculate():
    expression = st.session_state.expression.strip()

    # Do nothing if the input is empty
    if expression == "":
        return

    try:
        # Replace calculator symbols with Python symbols
        expression = expression.replace("^", "**")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace(" ", "")

        # Convert functions without brackets
        # Examples:
        # sin30 becomes sin(30)
        # sqrt16 becomes sqrt(16)
        expression = re.sub(
            r"\b(sin|cos|tan|sqrt|log|ln|exp)(-?\d+(?:\.\d+)?)",
            r"\1(\2)",
            expression
        )

        # Add multiplication automatically
        # Example: 23sin(30) becomes 23*sin(30)
        expression = re.sub(
            r"(\d|\))(?=(sin|cos|tan|sqrt|log|ln|exp)\()",
            r"\1*",
            expression
        )

        # Example: 2pi becomes 2*pi
        expression = re.sub(
            r"(\d|\))(?=(pi|e)\b)",
            r"\1*",
            expression
        )

        # Example: 2(3+4) becomes 2*(3+4)
        expression = re.sub(
            r"(\d|\))(?=\()",
            r"\1*",
            expression
        )

        # Mathematical functions allowed in the calculator
        allowed_functions = {
            "sin": sin_degree,
            "cos": cos_degree,
            "tan": tan_degree,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "exp": math.exp,
            "abs": abs,
            "pi": math.pi,
            "e": math.e,
            "pow": pow
        }

        # Calculate the result
        result = eval(
            expression,
            {"__builtins__": {}},
            allowed_functions
        )

        # Remove .0 from whole number results
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        # Round long decimal results
        if isinstance(result, float):
            result = round(result, 10)

        # Show result in the same input box
        st.session_state.expression = str(result)
        st.session_state.answer = str(result)

    except ZeroDivisionError:
        st.session_state.expression = "Error: Division by zero"

    except Exception:
        st.session_state.expression = "Error"


# Display the main heading
st.title(" Laiba Sehar ")

# Display a short description
st.caption("calculator")

st.divider()


# Calculator input field
st.text_input(
    "Enter calculation",
    key="expression",
    on_change=calculate
)


# First button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "C",
        on_click=clear_input,
        use_container_width=True
    )

with column2:
    st.button(
        "⌫",
        on_click=remove_last_character,
        use_container_width=True
    )

with column3:
    st.button(
        "(",
        on_click=add_value,
        args=("(",),
        use_container_width=True
    )

with column4:
    st.button(
        ")",
        on_click=add_value,
        args=(")",),
        use_container_width=True
    )


# Second button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "sin",
        on_click=add_value,
        args=("sin",),
        use_container_width=True
    )

with column2:
    st.button(
        "cos",
        on_click=add_value,
        args=("cos",),
        use_container_width=True
    )

with column3:
    st.button(
        "tan",
        on_click=add_value,
        args=("tan",),
        use_container_width=True
    )

with column4:
    st.button(
        "√",
        on_click=add_value,
        args=("sqrt",),
        use_container_width=True
    )


# Third button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "log",
        on_click=add_value,
        args=("log",),
        use_container_width=True
    )

with column2:
    st.button(
        "ln",
        on_click=add_value,
        args=("ln",),
        use_container_width=True
    )

with column3:
    st.button(
        "π",
        on_click=add_value,
        args=("pi",),
        use_container_width=True
    )

with column4:
    st.button(
        "e",
        on_click=add_value,
        args=("e",),
        use_container_width=True
    )


# Fourth button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "7",
        on_click=add_value,
        args=("7",),
        use_container_width=True
    )

with column2:
    st.button(
        "8",
        on_click=add_value,
        args=("8",),
        use_container_width=True
    )

with column3:
    st.button(
        "9",
        on_click=add_value,
        args=("9",),
        use_container_width=True
    )

with column4:
    st.button(
        "÷",
        on_click=add_value,
        args=("/",),
        use_container_width=True
    )


# Fifth button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "4",
        on_click=add_value,
        args=("4",),
        use_container_width=True
    )

with column2:
    st.button(
        "5",
        on_click=add_value,
        args=("5",),
        use_container_width=True
    )

with column3:
    st.button(
        "6",
        on_click=add_value,
        args=("6",),
        use_container_width=True
    )

with column4:
    st.button(
        "×",
        on_click=add_value,
        args=("*",),
        use_container_width=True
    )


# Sixth button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "1",
        on_click=add_value,
        args=("1",),
        use_container_width=True
    )

with column2:
    st.button(
        "2",
        on_click=add_value,
        args=("2",),
        use_container_width=True
    )

with column3:
    st.button(
        "3",
        on_click=add_value,
        args=("3",),
        use_container_width=True
    )

with column4:
    st.button(
        "-",
        on_click=add_value,
        args=("-",),
        use_container_width=True
    )


# Seventh button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "0",
        on_click=add_value,
        args=("0",),
        use_container_width=True
    )

with column2:
    st.button(
        ".",
        on_click=add_value,
        args=(".",),
        use_container_width=True
    )

with column3:
    st.button(
        "%",
        on_click=calculate_percentage,
        use_container_width=True
    )

with column4:
    st.button(
        "+",
        on_click=add_value,
        args=("+",),
        use_container_width=True
    )


# Eighth button row
column1, column2, column3, column4 = st.columns(4)

with column1:
    st.button(
        "x²",
        on_click=add_value,
        args=("**2",),
        use_container_width=True
    )

with column2:
    st.button(
        "xʸ",
        on_click=add_value,
        args=("**",),
        use_container_width=True
    )

with column3:
    st.button(
        "exp",
        on_click=add_value,
        args=("exp",),
        use_container_width=True
    )

with column4:
    st.button(
        "=",
        on_click=calculate,
        type="primary",
        use_container_width=True
    )