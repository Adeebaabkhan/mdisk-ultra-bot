# ph_indian_flag.py

# Define colors
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808"

def generate_receipt(student_name, college_name, amount, color_variation):
    """
    Generate a college receipt with the specified color variation.
    
    Parameters:
        student_name (str): Name of the student
        college_name (str): Name of the college
        amount (float): Amount to be paid
        color_variation (str): Color variation for the receipt background
    """
    colors = {
        "saffron": SAFFRON,
        "white": WHITE,
        "green": GREEN
    }
    
    # Select color based on variation
    bg_color = colors.get(color_variation, WHITE)
    
    receipt = f"""
    -------------------------------
               RECEIPT
    -------------------------------
    College: {college_name}
    Student: {student_name}
    Amount: ₹{amount:.2f}
    Background Color: {bg_color}
    -------------------------------
    """
    return receipt

# Sample usage
if __name__ == "__main__":
    print(generate_receipt("John Doe", "Indian College of Technology", 1500.00, "saffron"))
