import axios from 'axios'

import { RequestErrorInterceptor } from './interceptors/bad-request'
import SalonService from './services/salon'

const instance = axios.create({
  baseURL: import.meta.env.API_URL ?? 'http://localhost:8000/api/1.0.0',
})

RequestErrorInterceptor(instance)

export const api = {
  salon: SalonService(instance),
}
