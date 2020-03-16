Implementar uma rotina para controle de vouchers/ códigos promocionais.
Estes vouchers devem possuir campos que permitam seu controle, como:
- Data de validade: indicador de data limite para validade do voucher;
- Período: indica o período (em dias) pelo qual o voucher será válido após sua utilização;

Deve ser possível:
- Cadastrar novos vouchers;
- Ativar/ inativar vouchers;
- Remover vouchers;

Fluxo:

1º A Imersio cadastra um novo voucher. Este voucher possuirá:
- um usuário "pai", que será o usuário do nosso parceiro/ canal de venda
- data de validade (até quando ele será válido)
- tipo de voucher (inicialmente só teremos 1 tipo de voucher: 50% de comissão sobre o recorrente por até 12 meses, ou o usuário cancelar o plano - o que vier primeiro)

2º O usuário, ao efetuar o cadastro, informará o código do voucher, ficando assim "vinculado" ao cadastro do parceiro.

3º Se, a qualquer momento, o usuário adquirir um plano pago, o parceiro receberá a respectiva comissão pelo período acordado.

4º Na tela de cadastro de vouchers, será possível:
- Cadastrar novos vouchers (com os campos mencionados acima);
- Ativar voucher;
- Inativar vouchers;
- Excluir vouchers (que não possuam nenhum usuário vinculado);
- Listar quais usuários estão utilizando os vouchers listados;