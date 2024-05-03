function tocaSom (seletorAudio){
    const elemento = document.querySelector(seletorAudio);

    if(elemento != null && elemento.localName === 'audio'){
        elemento.play();
    } else{
            console.log('Elemento não encontrado ou seletor invalido');
    }
}

const listaDeTeclas = document.querySelectorAll('.tecla');

for (let contador = 0; contador < listaDeTeclas.length; contador ++) {

    const tecla = listaDeTeclas[contador];
    const instrumento = tecla.classList[1];
    const idAudio = `#som_${instrumento}`;//template string

    tecla.onclick = function() {
        tocaSom(idAudio);
    }
    //adiciona a classe ativa quando o usuário aperta a tecla
    tecla.onkeydown = function(evento){

        if (evento.code === 'Space' || evento.code === 'Enter') {
            tecla.classList.add('ativa')
        }
    }
    //removendo a classe ativa quando o usuário soltar a tecla
    tecla.onkeyup = function(){
        tecla.classList.remove('ativa');
    }

}
