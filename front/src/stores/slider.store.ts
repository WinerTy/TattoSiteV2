import { api } from '@/utils/api'
import type { Slider } from '@/utils/api/services/slider/slider.type'
import { defineStore } from 'pinia'

interface SliderState {
  sliders: Slider[]
  loading: boolean
  error: string | null
}

export const useSliderStore = defineStore('slider', {
  state: (): SliderState => ({
    sliders: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchSlider() {
      this.loading = true
      this.error = null

      try {
        this.sliders = (await api.slider.getSlider()).data.results
      } catch (error) {
        console.error(error)
        this.error = 'Error fetching salons'
      } finally {
        this.loading = false
      }
    },
  },
})
