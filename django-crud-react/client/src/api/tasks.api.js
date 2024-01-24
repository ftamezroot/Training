import axios from 'axios'

// Interactuamos con el backend
// axios es la bilbioteca que me permite hacer las peticiones
const taskApi = axios.create( {
    baseURL: "http://localhost:8000/tasks/api/v1/tasks/",
})

export const getAllTasks = () => taskApi.get("/");
export const createTask = (task) => taskApi.post("/", task);

// export const getAllTasks = () => {
//     return taskApi.get('/')
// }

// export const createTask = (task) => {
//     return taskApi.post('/', task)
// }