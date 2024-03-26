let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function consol() {
    console.log('o botao foi clicado')
}

function alerta() {
    alert("eu amo js")
}

function prompti() {
    let cidade = prompt("Qual o nome da sua cidade?")
    alert(`Eu já estive em ${cidade}`)
}

function somar() {
    let numero1 = prompt("Digite o primeiro numero")
    let numero2 = prompt("Digite o segundo numero")
    let somar = parseInt(numero1) + parseInt(numero2)
    alert("A soma é " + somar)
}