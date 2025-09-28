$(document).ready(function() {
    $('#expenseForm').on('submit', function(event) {
        // --- Amount Validation ---
        let amount = $('#amount').val();
        // Check if the amount is not a number or is less than or equal to zero
        if (isNaN(amount) || parseFloat(amount) <= 0) {
            // Prevent form submission
            event.preventDefault(); 
            
            // Show error message
            $('#amount').addClass('is-invalid');
            $('#amountError').show();
        } else {
            // If valid, remove error styling
            $('#amount').removeClass('is-invalid');
            $('#amountError').hide();
        }

        // Other validations (like for date and category) are handled by the `required` attribute in HTML5.
        // You could add more complex jQuery validation here if needed.
    });
});