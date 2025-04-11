# chatbot/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company, Product

@api_view(["POST"])
def conversation(request):
    """
    Conversational endpoint for ABC Lighting bot.
    Expects JSON payload: {"message": "<user message>"}
    """
    user_input = request.data.get("message", "").strip().lower()

    # 1. End-of-conversation check
    if user_input in ["no", "no thanks", "nothing"]:
        return Response({"response": "Could you please provide your contact information?"})
    
    # 2. Check for an exact product name match:
    products = Product.objects.all()
    for product in products:
        if product.name.lower() in user_input:
            image_html = (f"<br><img src='{product.image.url}' alt='{product.name}' style='max-width:200px;'>" 
                          if product.image else "")
            response_text = (
                f"Here are the details for our {product.name}:<br>"
                f"{product.description}<br>"
                f"Specs: {product.specs}<br>"
                f"Product Image:{image_html}<br>"
                "Is there anything else I can help you with?"
            )
            return Response({"response": response_text})
    
    # 3. Check for product-related keywords
    if "street light" in user_input:
        product = Product.objects.filter(product_type='street').first()
        if product:
            image_html = (f"<br><img src='{product.image.url}' alt='{product.name}' style='max-width:200px;'>" 
                          if product.image else "")
            response_text = (
                f"Here are the details for our {product.name}:<br>"
                f"{product.description}<br>"
                f"Specs: {product.specs}<br>"
                f"Product Image:{image_html}<br>"
                "Is there anything else I can help you with?"
            )
        else:
            response_text = "Sorry, we currently do not have details for the Solar Powered Street Light."
        return Response({"response": response_text})

    if "driveway light" in user_input:
        product = Product.objects.filter(product_type='driveway').first()
        if product:
            image_html = (f"<br><img src='{product.image.url}' alt='{product.name}' style='max-width:200px;'>" 
                          if product.image else "")
            response_text = (
                f"Here are the details for our {product.name}:<br>"
                f"{product.description}<br>"
                f"Specs: {product.specs}<br>"
                f"Product Image:{image_html}<br>"
                "Is there anything else I can help you with?"
            )
        else:
            response_text = "Sorry, we currently do not have details for the Solar Powered Driveway Light."
        return Response({"response": response_text})

    if "wall light" in user_input:
        product = Product.objects.filter(product_type='wall').first()
        if product:
            image_html = (f"<br><img src='{product.image.url}' alt='{product.name}' style='max-width:200px;'>" 
                          if product.image else "")
            response_text = (
                f"Here are the details for our {product.name}:<br>"
                f"{product.description}<br>"
                f"Specs: {product.specs}<br>"
                f"Product Image:{image_html}<br>"
                "Is there anything else I can help you with?"
            )
        else:
            response_text = "Sorry, we currently do not have details for the Solar Powered Outside Wall Light."
        return Response({"response": response_text})

    # 4. General product query
    if "products" in user_input or "product" in user_input:
        all_products = products
        if all_products.exists():
            product_list_text = "Here are the products we currently offer:<br>"
            for idx, p in enumerate(all_products, 1):
                product_list_text += f"{idx}. {p.name}<br>"
            product_list_text += (
                "<br>If you'd like details on a specific product, try saying for example: "
                "\"Tell me about the street light\" or \"Show me the driveway light.\""
            )
            product_list_text += "<br>Is there anything else I can help you with?"
        else:
            product_list_text = "We currently have no products listed. Please check back later."
        return Response({"response": product_list_text})
    
    # 5. Check for company information queries
    if "company info" in user_input or ("about" in user_input and "light" not in user_input) or "company" in user_input:
        company = Company.objects.first()
        if company:
            response_text = (
                f"{company.name}<br>"
                f"{company.description}<br>"
                f"Locations: {company.locations}<br>"
                f"Business Hours: {company.business_hours}<br>"
                "Is there anything else I can help you with?"
            )
        else:
            response_text = "Sorry, company information is not available at the moment."
        return Response({"response": response_text})
    
    # 6. Default response
    default_response = "How may I assist you today? Is there anything else I can help you with?"
    return Response({"response": default_response})

def chat_interface(request):
    """
    Render the chatbot UI.
    """
    return render(request, "chatbot/chat.html")
