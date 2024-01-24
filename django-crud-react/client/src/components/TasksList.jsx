import { useEffect, useState } from "react"
import { getAllTasks } from "../api/tasks.api"
import { TaskCard } from "./TaskCard";

export function TasksList() {
  // Guardamos los datos que obteneos del backend con useState
  const [tasks, setTasks] = useState([]);

  // Apenas cargue la página, realice lo siguiente
  useEffect( () => {
    // async para decirle que se va a estar ejecutando en paralelo con otras operaciones
    // await para que espera a obtener la respuesta
    async function loadTaks() {
        const res = await getAllTasks();
        // Le pasamos los valores a la variable tasks
        setTasks(res.data);
    }
    loadTaks()

  }, []);
  return <div>
    {tasks.map(task => (
        <TaskCard key={task.id} task={task} />
    ))}
  </div>
}
