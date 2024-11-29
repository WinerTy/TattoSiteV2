import type { AxiosInstance, AxiosPromise } from 'axios'
import type { Salon } from './salon.type'
import type { ApiResponse } from '../base.type'

export default (instance: AxiosInstance) => ({
  getSalons(): AxiosPromise<ApiResponse<Salon>> {
    return instance.get('/salon/')
  },
})
