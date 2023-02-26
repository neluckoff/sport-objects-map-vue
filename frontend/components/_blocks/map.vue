<template>
    <div class="container">
        <div class="row">
            <div class="col-xxl-12">
                <div class="chooser">
                    <div class="chooser__map">
                        <select v-model="selected">
                            <option>Спутниковая</option>
                            <option>Географическая</option>
                        </select>
                    </div>
                </div>
                <div class="map">
                    <client-only>
                        <v-map :zoom=" options.minZoom" :center="[61.374, 63.5594]" class="map__object">
                            <v-icondefault></v-icondefault>
                            <l-tile-layer :url="map" :options="options"></l-tile-layer>
                            <v-marker-cluster>
                                <template v-for="(item, i) in items">
                                    <v-marker :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i"></v-marker>
                                </template>
                            </v-marker-cluster>
                            <!-- <l-marker :lat-lng="[61.374, 63.5594]">
                                <l-icon>
                                    <div class="marker">
                                        <div class="marker-icon">
                                            <base-svg name="location"></base-svg>
                                        </div>
                                    </div>
                                </l-icon> 
                            </l-marker> -->
                            <div v-show="false" class="map__information">

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
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // components: {
    //     'v-marker-cluster': Vue2LeafletMarkerCluster
    // },
    data: () => ({
		items: [],
        options: {
            minZoom: 3,
            maxZoom: 17,
        },
        map: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", //https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
        selected: "Спутниковая",
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
	},
    watch: {
        selected(newValue, oldValue) {
            if (newValue === "Спутниковая") {
                this.map = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
            } else {
                this.map = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            }
        },
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
        width: 30%;
        height: 100%;
        background-color: white;
        z-index: 999;
        border-radius: 20px;
    }
}
</style>
  