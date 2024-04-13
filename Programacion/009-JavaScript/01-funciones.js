const esto = (valor) => {
    console.log ("Funcion: esto");

    const esIgual = (otro) => {
        console.log ("Funcion: esIgual");

        if (otro == valor){
            return console.log ("exitoso :", otro == valor)

        } else {
            return console.log ("exitoso :", otro == valor, "causa: No es igual")
        }
    };

    const noEsIgual = (otro) => {
        console.log ("Funcion: noEsIgual");

        if (otro != valor){
            return console.log ("exitoso :", otro != valor)

        } else {
            return console.log ("exitoso :", otro != valor, "causa: Es igual")
        }
    }

    return {
        esIgual,
        noEsIgual,
    };
}

/* 
Cambiar resultado a un objeto.
Posibles valores:
    - { exitoso: true }
    - { exitoso: false, causa: "No es igual" }
    - { exitoso: false, causa: "Es igual" }
*/
esto (5).esIgual (5);  // { exitoso: true }
esto (5).esIgual (10); // { exitoso: false, causa: " No es igual " }

esto ("Hola").noEsIgual ("Chau"); // { exitoso: true }
esto ("Hola").noEsIgual ("Hola"); // { exitoso: false, causa: "Es igual" }