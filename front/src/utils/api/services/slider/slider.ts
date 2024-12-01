import type { AxiosInstance, AxiosPromise } from 'axios'
import type { ApiResponse } from '../../base/base.type'
import type { Slider } from './slider.type'

export default (instance: AxiosInstance) => ({
  getSlider(): AxiosPromise<ApiResponse<Slider>> {
    return instance.get('/slider/')
  },
})
