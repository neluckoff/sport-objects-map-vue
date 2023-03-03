<template>
    <div class="map">
        <div class="map__info">
            <div class="header">
                <div class="header__left">
                    <div class="header__image">
                        <base-svg name="map"></base-svg>
                    </div>
                    <div class="header__text">
                        <span class="header__text-basic">
                            <span class="header__text-red">Sport</span> 
                            Objects Map
                        </span>
                    </div>
                </div>
                <!-- <div v-if="cardItem != null" class="btn btn-secondary" @click="cardItem = null">
                    <span>Назад</span>
                </div> -->
            </div>
            <cards-object v-if="cardItem!=null" :cardItem="cardItem" :showGraph="showGraph"></cards-object>
            <div class="settings" v-else>
                <span class="settings__text">Настройка карты</span>
                <div class="settings__map select-wrapper">
                    <select v-model="mapSelected" class="select">
                        <option>Спутниковая</option>
                        <option>Географическая</option>
                        <option>Гибридная</option>
                        <option>Рельефная</option>
                    </select>
                </div>
                <div class="settings__checkboxes">
                    <base-checkbox v-model="pointGroup" class="checkbox">
                        <p>Группировка объектов</p>
                    </base-checkbox>
                </div>
            </div>
        </div>
        
        <div class="map__window">
            <div class="map__window-block">
                <client-only>
                    <v-map :zoom=" options.minZoom" :center="center" class="map__object">
                        <v-icondefault></v-icondefault>
                        <l-tile-layer :url="map" :options="options"></l-tile-layer>
                        <v-marker-cluster v-if="pointGroup">
                            <template v-for="(item, i) in items">
                                <v-marker @click="openDesc(item)" :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i">
                                    <l-icon>
                                        <div class="marker">
                                            <div class="marker-icon">
                                                <base-marker name="dumbbell"></base-marker>
                                            </div>
                                        </div>
                                    </l-icon>
                                </v-marker>
                            </template>
                        </v-marker-cluster>
                        <template v-for="(item, i) in items" v-else>
                            <v-marker @click="openDesc(item)" :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i">
                                <l-icon>
                                    <div class="marker">
                                        <div class="marker-icon">
                                            <base-marker name="dumbbell"></base-marker>
                                        </div>
                                    </div>
                                </l-icon>
                            </v-marker>
                        </template>
                        
                        <div class="map__window-infos">
                            <span>Объектов на карте: {{ items.length }}</span>
                        </div>
                    </v-map>
                </client-only>
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
            subdomains:['mt0','mt1','mt2','mt3'],
            // maxBoundsViscosity: 1,
            // bounds: [[-89.98155760646617,  -180 ], [89.99346179538875, 180]]
        },
        center: [61.374, 63.5594],
        map: 'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', //https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png // 'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}'
        mapSelected: "Спутниковая",
        pointGroup: true,
        cardItem: null,
        showGraph: true,
	}),
	methods: {
		async fetch() {
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/objects/open`,
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
            this.cardItem = item;
            // this.center = [item.coordinates.lat, item.coordinates.lng];
            this.reloadManual()
        },

        reloadManual() {
            this.showGraph = false;
            this.$nextTick(() => {
                this.showGraph = true;
            });
        },
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
    },
	mounted() {
		this.fetch()
	}
}
</script>

<style lang="scss" scoped>
.map {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    // flex-wrap: nowrap;

    .marker {
        .svg {
            box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
            background-color: $color-3;
            padding: 5px;
            border-radius: 50%;
            border: 2px solid rgba(33, 33, 33, 0.5);

            width: 26px;
            height: 26px;

            :deep() svg {
                max-width: 100%;
                max-height: 100%;
            }

            &:hover {
                opacity: 0.8;
            }
        }
    }

    &__info {
        overflow: auto;
        width: 30%;
        height: 100%;
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        z-index: 2;
        padding: 20px;

        .header {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: space-between;
            padding-bottom: 10px;

            &__left {
                padding-bottom: 10px;
                width: 100%;
                border-bottom: 1px solid $color-5;
                display: flex;
                flex-direction: row;
                align-items: center;
            }

            &__image {
                margin-right: 20px;

                .svg {
                    width: 48px;
                    height: auto;
                    
                    :deep() svg {
                        fill: $color-3;
                    }
                }
            }

            &__text {
                &-basic {
                    color: #212121;
                    font-size: 22px;
                    font-weight: 600;
                }

                &-red {
                    font-size: 22px;
                    color: $color-3;
                }
            }
        }

        .settings {
            margin-top: 20px;
            width: 100%;
            display: flex;
            flex-direction: column;

            &__text {
                color: #212121;
                font-weight: 600;
                font-size: 20px;
            }

            &__map {
                margin-top: 10px;
            }

            &__checkboxes {
                padding-top: 10px;
            }
        }
    }

    &__window {
        width: 100%;
        height: 100%;
        z-index: 1;

        &-block {
            width: 100%;
            height: 100%;

            :deep(.leaflet-container) {
            .leaflet-control-attribution {
                display: none !important;
            }
            // .leaflet-control-zoom {
            // 	display: none;
            // }
	        }
        }

        &-infos {
            position: absolute;
            border-radius: 20px 20px 0 0;
            right: 20px;
            bottom: 0px;
            z-index: 999;
            padding: 10px 20px;
            background-color: #fff;
            box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);

            span {
                color: #808080;
                font-size: 16px;
                font-weight: 500;
            }
        }
    }
}
</style>