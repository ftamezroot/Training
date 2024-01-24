import {useForm} from 'react-hook-form'
import { createTask } from '../api/tasks.api'
import { useNavigate} from 'react-router-dom'

// Con jup y zod podemos hacer validaciones más complejas
// pero por ahora utilizaremos useForm

export function TaskFormPage() {

  const {register, handleSubmit, formState: {errors} } = useForm();
  const navigate = useNavigate();

  const onSubmit = handleSubmit( async data => {
    const res = await createTask(data);
    navigate("/tasks");
  })

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input 
          type="text" 
          placeholder="title" 
          {...register("title", { required: true })}
        />
        {errors.title && <span>This field is required.</span>}

        <textarea
          name="descreiption" 
          rows="3" 
          placeholder="Description"
          {...register("description", { required: true })}
        />
        {errors.description && <span>This field is required.</span>}
        <button>Save</button>
      </form>
    </div>
  )
}