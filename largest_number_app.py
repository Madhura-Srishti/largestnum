import streamlit as st

def find_largest_number(a, b, c):
    numbers = [a, b, c]
    return max(numbers)

def main():
    st.title("Find the largest number")

    # Input the three numbers
    num1 = st.number_input("Enter the first number :", value=0.0,min_value=-200000000.0,max_value=200000000.0)
    num2 = st.number_input("Enter the second number :", value=0.0,min_value=-200000000.0,max_value=200000000.0)
    num3 = st.number_input("Enter the third number :", value=0.0,min_value=-200000000.0,max_value=200000000.0)

    # Find the largest number
    largest_number = find_largest_number(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is : {largest_number}")

if __name__ == "__main__":
    main()
