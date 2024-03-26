alert("Boas Vindas ao jogo do número secreto");

let numeroSecreto  = parseInt(Math.random() *100 + 1);

let chute;

let tentativas = 1;

while (chute != numeroSecreto) {

    chute = prompt("Escolha um numero entre 0 e 100");

    if (chute == numeroSecreto) {
        break;
    } else {
          if (chute > numeroSecreto) {
                alert("O numero secreto é menor");
            } else {
                alert("O numero secreto é maior");
            }
            // tentativas = tentativas =1
            tentativas++;
    }
}

// Operador ternário
let palavraTentativa = tentativas >  1 ? "tentativas" : "tentativa";
alert(`Parabéns você acertou o número! ${numeroSecreto} com ${tentativas} ${palavraTentativa}`);

// if (tentativas > 1) {
//     alert(`Parabéns você acertou o número! ${numeroSecreto} com ${tentativas} tentativas`);
// } else {
//     alert(`Parabéns você acertou o número! ${numeroSecreto} com ${tentativas} tentativa`);
// }
           