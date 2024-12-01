import axios from 'axios'

import { RequestErrorInterceptor } from './interceptors/bad-request'
import SalonService from './services/salon/salon'
import SliderService from './services/slider/slider'
import MasterService from './services/masters/masters'
import TagsService from './services/tags/tags'
const instance = axios.create({
  baseURL: import.meta.env.API_URL ?? 'http://localhost:8000/api/1.0.0',
})

RequestErrorInterceptor(instance)

export const api = {
  salon: SalonService(instance),
  slider: SliderService(instance),
  master: MasterService(instance),
  tags: TagsService(instance),
}
