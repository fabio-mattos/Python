from flask import Flask, send_file
import qrcode

app = Flask(__name__)

@app.route('/qrcode/<content>')
def generate_qrcode(content):
    # Gerar o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Salvar o QR Code em um arquivo temporário
    temp_img_path = 'temp_qrcode.png'
    img.save(temp_img_path)

    # Enviar o arquivo de volta como resposta
    return send_file(temp_img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)