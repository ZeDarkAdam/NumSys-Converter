import streamlit as st

st.set_page_config(
    page_title="NumSys Converter",
    page_icon= "🔢",
    layout="centered" # wide, centered
)

hide_st_style = """
            <style>
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_st_style, unsafe_allow_html=True)


def convert_number(number, from_base, to_base):
    # Переведення у десяткову систему
    if from_base != 10:
        decimal_number = int(str(number), from_base)
    else:
        decimal_number = number

    # Переведення з десяткової системи в іншу
    if to_base == 10:
        result = decimal_number
    else:
        result = format(decimal_number, 'x') if to_base == 16 else format(decimal_number, f'0{len(str(decimal_number))}o') if to_base == 8 else bin(decimal_number)[2:]

    return result


def has_only_digits(input_str):
    return input_str.isdigit()


def is_binary(number_to_convert):
    for digit in number_to_convert:
        if digit not in ('0', '1'):
            return False
    return True


def is_octal(number_to_convert):
    for digit in number_to_convert:
        if digit not in ('0', '1', '2', '3', '4', '5', '6', '7'):
            return False
    return True


def is_decimal(number_to_convert):
    if number_to_convert.isdigit():
        return True
    else:
        return False
    

def is_hexadecimal(number_to_convert):
    valid_hex_chars = set("0123456789ABCDEFabcdef")

    for char in number_to_convert:
        if char not in valid_hex_chars:
            return False
    return True


def is_from_base(number_to_convert, from_base):

    if from_base == 2:
        return is_binary(number_to_convert)
    
    if from_base == 8:
        return is_octal(number_to_convert)

    if from_base == 10:
        return is_decimal(number_to_convert)
    
    if from_base == 16:
        return is_hexadecimal(number_to_convert)


def convert(number_to_convert):
        if has_only_digits(number_to_convert):
            int_num = int(number_to_convert)
        else:
            int_num = number_to_convert
        

        st.write("Результат конвертації:")
        result = convert_number(int_num, from_base, to_base)

        if isinstance(result, str):
            code = result.upper()
        else:    
            code = int(result)

        return (str(code))


number_to_convert = st.text_input("Введіть число для конвертації: ", value = None)

col1, col2, = st.columns([1, 1])
with col1:
    from_base = int(st.selectbox('Початкова система числення', ('2', '8', '10', '16'), index = 2))

with col2:
    to_base = int(st.selectbox('Кінцева система числення', ('2', '8', '10', '16'), index = 0))


error_message = "Введіть число для конвертації"
if number_to_convert is not None: 
    if number_to_convert == "":
        st.error(error_message)
    else:
        if is_from_base(number_to_convert, from_base):
            code = convert(number_to_convert)
            st.code(code)
        else:
            st.error("Невірний ввід")
else:
    st.error(error_message)
    
