import type { AxiosInstance, AxiosPromise } from 'axios'
import type { Master, MasterParams } from './masters.type'
import type { ApiResponse } from '../../base/base.type'

export default (instance: AxiosInstance) => ({
  getMasters(params: MasterParams): AxiosPromise<ApiResponse<Master>> {
    return instance.get(`/master/`, { params })
  },
})
