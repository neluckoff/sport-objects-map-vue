import Vue from 'vue'
import { Line, Pie, Bar, Doughnut } from 'vue-chartjs/legacy'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  ArcElement
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  BarElement,
  CategoryScale,
  LinearScale,
  LineElement,
  ArcElement
)

Vue.component('line-chartjs', {
  extends: Line
})

Vue.component('pie-chartjs', {
    extends: Pie
})

Vue.component('bar-chartjs', {
    extends: Bar
})

Vue.component('doughnut-chartjs', {
  extends: Doughnut
})