from pyscript import document, display

def order(e):

# Prices
  # Snacks
  chips = 5.00
  biscuits = 2.50
  gummies = 2.00

    # Drinks
  soda = 1.50
  water = 1.50
  juice = 1.50

  # Detecting the checkboxes

    # Snacks
  chips_ordered = int(document.getElementById("chips").checked)
  biscuits_ordered = document.getElementById("biscuits").checked
  gummies_ordered = document.getElementById("gummies").checked

    # Drinks
  soda_ordered = document.getElementById("soda").checked
  water_ordered = document.getElementById("water").checked
  juice_ordered = document.getElementById("juice").checked

  # Calculating (w/ Booleans returning 1s and 0s)
  subtotal = (
    chips * chips_ordered +
    biscuits * biscuits_ordered +
    gummies * gummies_ordered + 
    soda * soda_ordered +
    water * water_ordered +
    juice * juice_ordered
  )

  # 12% vat
  vat = subtotal * 0.12

  # After vat
  total = subtotal + vat

  #  Displaying the receipt
  document.getElementById("subtotal").innerText = f"${subtotal}"
  document.getElementById("vat").innerText = f"${vat}"
  document.getElementById("total").innerText = f"${total}"