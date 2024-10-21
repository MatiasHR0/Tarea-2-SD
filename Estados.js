// Tenemos un semaforo, y tenemos que plantear una maquina de estados
// Para las distintas luces del semaforo

const states = {
    Procesando : {
        on : {
            next: 'Preparado',
        }
    },
    Preparado: {
        on : {
            next: 'Enviado',
            
        }
    },
    Enviado: {
        on: {
            next: 'Entregado',

        }
    },
    Entregado: {
        on: {
            next: 'Finalizado',
        }
    },
    Finalizado: {
        on: {
            previous: 'Entregado'
        }
    }
}


class FiniteStateMachine{
    constructor(state, states){
        this.state = state;
        this.states = states;
    }

    async transition(event){
        const nextState = this.states[this.state].on[event]
               if(nextState){
            this.state = nextState
        } else {
            throw new Error('Unhandled state')
        }
    }

    getCurrentState(){
        return this.state
    }
}


const semaphore = new FiniteStateMachine('Procesado', states)

console.log(Estadoactual: ${semaphore.getCurrentState()})

semaphore.transition('next')

console.log(Estadoactual: ${semaphore.getCurrentState()})