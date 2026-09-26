from pyscript import document, display

def generate_sku(e):
  category = document.getElementById('category').value
  product = document.getElementById('pr_name').value
  quantity = document.getElementById('quantity').value

  product_code = product[:3].upper()
  quantity_code = f"{int(quantity):03}"

  sku = f"{category}-{product_code}-{quantity_code}"
  document.getElementById('sku').innerText = sku