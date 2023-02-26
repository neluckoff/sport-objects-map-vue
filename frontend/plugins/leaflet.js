import Vue from 'vue'
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'
import * as Vue2Leaflet from 'vue2-leaflet'

Vue.component('v-marker-cluster', Vue2LeafletMarkerCluster)
Vue.component('v-icondefault', Vue2Leaflet.LIconDefault)
Vue.component('v-tilelayer', Vue2Leaflet.LTileLayer)
Vue.component('v-map', Vue2Leaflet.LMap)
Vue.component('v-marker', Vue2Leaflet.LMarker)