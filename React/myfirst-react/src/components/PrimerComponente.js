import React, {useState} from 'react'

export const PrimerComponente = () => {
    let cursos = ['Algebra', 'Compu', 'Geometria'];
    // let minombre = 'Fabio Tamez'

    const [minombre, setNombre] = useState("Fabio");

    const cambiarNombre = (nuevoNombre) => {
        setNombre(nuevoNombre);
    }

  return (
    <div>PrimerComponente
        <p>Mi nombre es: <strong className={minombre.length >= 4 ? 'verde' : 'rojo'}>{minombre}</strong></p>
        <input type="text" onChange={e => cambiarNombre(e.target.value)} placeholder='Cambiar'/>
        <button onClick={ e => cambiarNombre("Fabio Manuel Tamez")}>Cambiar nombre</button>
        

        <h2>Cursos</h2>
        <ul>
            {
                cursos.map( (curso, indice) => {
                    return (<li key={indice}>
                        {curso}
                    </li>)
                })
            }
        </ul>

    </div>
  )
}
