<template>
    <div class="container">
        <div class="row">
            <div class="col-xxl-12">
                <div class="chooser">
                    <div class="chooser__map">
                        <select v-model="mapSelected">
                            <option>Спутниковая</option>
                            <option>Географическая</option>
                            <option>Гибридная</option>
                            <option>Рельефная</option>
                        </select>
                    </div>
                    <div>
                        <input v-model="pointGroup" type="checkbox" id="scales" name="scales" checked>
                        <label for="scales">Scales</label>
                    </div>
                </div>
                <div class="map">
                    <client-only>
                        <v-map :zoom=" options.minZoom" :center="[61.374, 63.5594]" class="map__object">
                            <v-icondefault></v-icondefault>
                            <l-tile-layer :url="map" :options="options"></l-tile-layer>
                            <v-marker-cluster v-if="pointGroup">
                                <template v-for="(item, i) in items">
                                    <v-marker @click="openDesc(item)" :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i"></v-marker>
                                </template>
                            </v-marker-cluster>
                            <template v-for="(item, i) in items" v-else>
                                <v-marker :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i"></v-marker>
                            </template>
                            <!-- <l-marker :lat-lng="[61.374, 63.5594]">
                                <l-icon>
                                    <div class="marker">
                                        <div class="marker-icon">
                                            <base-svg name="location"></base-svg>
                                        </div>
                                    </div>
                                </l-icon> 
                            </l-marker> -->
                            <div class="map__information" v-if="cardItem!=null">
                                <h4>{{ cardItem.name }}</h4>
                                <span>{{ cardItem.desc }}</span>
                                <span>Тип: {{ cardItem.objectType }}</span>
                                <span>Виды спорта: {{ cardItem.sportType }}</span>

                                <span>Действие с объектом: {{ cardItem.action }}</span>
                                <span>Адресс: {{ cardItem.address }}</span>
                                <span>Активный: {{ cardItem.active }}</span>
                            </div>
                        </v-map>
                    </client-only>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-xxl-12">
                <div>Точек на карте сейчас: {{ items.length }}</div>
                <div>{{ map }}</div>
                <div>{{ pointGroup }}</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
		items: [],
        options: {
            minZoom: 3,
            maxZoom: 17,
            subdomains:['mt0','mt1','mt2','mt3']
        },
        map: 'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', //https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
        mapSelected: "Спутниковая",
        pointGroup: true,
        cardItem: null,
	}),
	methods: {
		async fetch() {
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/objects`,
						{}
					);
					if (response) {
						this.items = response;
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
        async openDesc(item) {
            this.cardItem = item
        }
	},
    watch: {
        mapSelected(newValue, oldValue) {
            if (newValue === "Спутниковая") {
                this.map = "http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
            } else if (newValue === "Географическая") {
                this.map = "http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            } else if (newValue === "Гибридная") {
                this.map = "http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}"
            } else if (newValue === "Рельефная") {
                this.map = "http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
            }
        },
        pointGroup() {

        }
    },
	mounted() {
		this.fetch()
	}
}
</script>

<style lang="scss" scoped>
.chooser {
    width: 100%;
    display: flex;
    flex-direction: row;

    &__map {

        select {
            padding: 10px 20px;
            border-radius: 20px;
        }
    }
}
.map {
    margin-top: 20px;
    width: 100%;
    height: calc(100vh - 250px);

    :deep(.leaflet-container) {
		.leaflet-control-attribution {
			display: none !important;
		}
		// .leaflet-control-zoom {
		// 	display: none;
		// }
	}

    &__object {
        width: 100%;
        padding: 20px;
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
    }

    &__information {
        position: relative;
        width: 35%;
        height: 100%;
        background-color: white;
        z-index: 999;
        border-radius: 20px;
        padding: 20px;
        display: flex;
        flex-direction: column;
    }
}

</style>
  