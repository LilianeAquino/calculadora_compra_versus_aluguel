import os
from flask import Flask, request, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

from modules.calculator import calcular_valor_total_aluguel, calcular_valor_total_investimento, calcular_valorizacao_imovel, decisao_comprar_ou_alugar


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.template_folder = 'templates'

class FormCalc(FlaskForm):
    valor_mensal_aluguel = FloatField('Aluguel Mensal', validators=[InputRequired()])
    valor_compra_imovel = FloatField('Valor Imóvel', validators=[InputRequired()])
    taxa_valorizacao_imovel = FloatField('Valorização Imóvel (em %)', validators=[InputRequired(), NumberRange(min=0)])
    taxa_aumento_aluguel = FloatField('Atualização Aluguel (em %)', validators=[InputRequired(), NumberRange(min=0)])
    taxa_juros_aplicacao = FloatField('Juros Aplicação (em %)', validators=[InputRequired(), NumberRange(min=0)])
    botao_calcular = SubmitField('Calcular')


@app.route('/', methods=['GET', 'POST'])
def calculator():
    form = FormCalc()

    if form.validate_on_submit():
        valor_mensal_aluguel = form.valor_mensal_aluguel.data
        valor_compra_imovel = form.valor_compra_imovel.data
        taxa_valorizacao_imovel = form.taxa_valorizacao_imovel.data
        taxa_aumento_aluguel = form.taxa_aumento_aluguel.data
        taxa_juros_aplicacao = form.taxa_juros_aplicacao.data

        valor_total_aluguel = calcular_valor_total_aluguel(valor_mensal_aluguel, taxa_aumento_aluguel)
        valor_total_investido = calcular_valor_total_investimento(valor_compra_imovel, taxa_juros_aplicacao)
        valor_total_investido_lucro = round(valor_total_investido - valor_compra_imovel, 2)
        valor_imovel = calcular_valorizacao_imovel(valor_compra_imovel, taxa_valorizacao_imovel)

        decisao = decisao_comprar_ou_alugar(valor_total_aluguel, valor_total_investido, valor_imovel)

        return render_template('resultado.html', valor_total_aluguel=valor_total_aluguel, valor_imovel=valor_imovel,
                               valor_total_investido=valor_total_investido_lucro, decisao=decisao, form=form)
    return render_template('calcimobiliaria.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
