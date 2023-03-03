<template>
    <section>
        <transition name="fade-width">
            <div class="object" v-if="cardItem!=null">
                <cards-object :cardItem="cardItem" :showGraph="showGraph"></cards-object>
            </div>
        </transition>
        <div class="map">
            <client-only>
                <div class="header">
                    <div class="header__left">
                        <div class="header__image">
                            <base-svg name="map"></base-svg>
                        </div>
                        <div class="header__text">
                            <span class="header__text-basic">
                                <span class="header__text-red">Карта</span> 
                                Спорта
                            </span>
                        </div>
                    </div>
                    <div class="header__settings">
                        <base-svg name="search"></base-svg>
                    </div>
                </div>
                <div class="settings">
                    <div class="settings__logo" @click="settings()">
                        <base-svg name="gear"></base-svg>
                    </div>
                    <transition name="fade-height">
                        <div class="settings__params" v-if="showSettings == true">
                            <div class="settings__span">
                                <span>Настройки карты</span>
                            </div>
                            <div class="settings__params-map select-wrapper">
                                <select v-model="mapSelected" class="select">
                                    <option>Спутниковая</option>
                                    <option>Географическая</option>
                                    <option>Гибридная</option>
                                    <option>Рельефная</option>
                                </select>
                            </div>
                            <div class="settings__params-checkboxes">
                                <base-checkbox v-model="pointGroup" class="checkbox">
                                    <p>Группировка объектов</p>
                                </base-checkbox>
                            </div>
                        </div>
                    </transition>
                </div>
                <transition name="fade-height">
                    <div class="close-info" @click="closeDesc()" v-if="cardItem != null">
                        <base-svg name="chevron-left"></base-svg>
                    </div>
                </transition>
                <div class="num-objects">
                    <base-svg name="house"></base-svg>
                    <span>{{ items.length }}</span>
                </div>
                <v-map :zoom=" options.minZoom" :center="center" ref="map" @update:zoom="zoomUpdate">
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
                </v-map>
            </client-only>
        </div>
    </section>
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
        showSettings: false,
        currentZoom: null,
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
            if (this.cardItem == null) {
                this.cardItem = item;
                setTimeout(() => {
                    this.reloadMap();
                }, 1000);
            } else {
                this.cardItem = item;
                this.reloadMap();
            }
            this.reloadManual()
            document.title = `${this.cardItem.name} - Карта Спорта`
        },
        async reloadManual() {
            this.showGraph = false;
            this.$nextTick(() => {
                this.showGraph = true;
            });
        },
        async closeDesc() {
            this.cardItem = null;
            this.$refs.map.mapObject.invalidateSize(true);
            document.title = `Карта Спорта`
        },
        async reloadMap() {
            this.$refs.map.mapObject.invalidateSize(true);
            this.$refs.map.mapObject.setView([this.cardItem.coordinates.lat, this.cardItem.coordinates.lng], this.currentZoom, {
                animate: true,
                duration: 1.0,
                
            });
        },
        async zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        async settings() {
            if (this.showSettings == false) {
                this.showSettings = true;
            } else {
                this.showSettings = false;
            }
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
    },
	mounted() {
		this.fetch()
	}
}
</script>

<style lang="scss" scoped>
section {
    display: flex;
    flex-direction: row;
}

.num-objects {
    display: flex;
    position: absolute;
    flex-direction: row;
    z-index: 999;
    bottom: 20px;
    right: 30px;
    background-color: white;
    padding: 10px 15px;
    border-radius: 20px;
    align-items: center;

    span {
        padding-left: 10px;
        color: $color-5;
        font-size: 18px;
        font-weight: 500;
    }

    .svg {
        width: 28px;
        height: auto;
        
        :deep() svg {
            fill: $color-3;
        }
    }
}

.fade-width-enter-active, .fade-width-leave-active {
  transition: all 1s;
  max-width: 30%;
}
.fade-width-enter, .fade-width-leave-to {
  opacity: 0;
  max-width: 0px;
}

.fade-height-enter-active, .fade-height-leave-active {
  transition: all 0.8s;
  max-height: 30%;
}
.fade-height-enter, .fade-height-leave-to {
  opacity: 0;
  max-height: 0px;
}

.close-info {
    position: absolute;
    z-index: 999;
    margin: auto;
    position: absolute;
    bottom: 20px;
    left: 30px;
    padding: 10px;
    background-color: $color-1;
    cursor: pointer;
    border-radius: 20px;
    transition: all .2s ease-out;

    .svg {
        width: 20px;
        height: auto;
        
        :deep() svg {
            fill: $color-3;
        }
    }

    &:hover {
        opacity: 0.8;
    }
}

.object {
    overflow-y: auto;
    overflow-x: hidden;;
    box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
    border-radius: 20px 0 0 20px;
    right: 0;
    height: 100vh;
    width: 30%;
    background-color: $color-1;
    padding: 20px;
}

.settings {
    z-index: 999;
    position: absolute;
    right: 30px;
    top: 20px;
    transition: all .2s ease-out;
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    &__span {
        padding-bottom: 5px;

        span { 
            color: $color-5;
        }
    }

    &__params {
        margin-top: 10px;
        padding: 20px;
        background-color: $color-1;
        border-radius: 20px;
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);

        &-map {
            margin-bottom: 7px;;
        }

        &-checkboxes {
            border-top: 1px solid $color-5;
            padding: 7px 0;
        }
    }

    &__logo {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        padding: 10px;
        background-color: $color-1;
        border-radius: 20px;
        cursor: pointer;

        &:hover {
            opacity: 0.8;
        }
        .svg {
            width: 100%;
            height: 100%;
            justify-content: center;
            align-items: center;
            
            :deep() svg {
                fill: $color-3;
                width: 28px;
                height: auto;
            }
        }
    }
}

.header {
    top: 20px;
    left: 30px;
    z-index: 999;
    position: absolute;
    display: flex;
    flex-direction: row;
    align-items: center;

    &__settings {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        padding: 10px;
        background-color: $color-1;
        height: 100%;
        border-radius: 20px;
        margin-left: 10px;
        cursor: pointer;
        transition: all .2s ease-out;

        .svg {
            width: 28px;
            height: auto;
            
            :deep() svg {
                fill: $color-3;
            }
        }

        &:hover {
            opacity: 0.8;
        }
    }

    &__left {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        padding: 0 20px;
        height: 48px;
        background-color: $color-1;
        border-radius: 20px;
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    &__image {
        margin-right: 20px;

        .svg {
            width: 30px;
            height: auto;
            
            :deep() svg {
                fill: $color-3;
            }
        }
    }

    &__text {
        &-basic {
            color: #212121;
            font-size: 20px;
            font-weight: 600;
        }

        &-red {
            font-size: 20px;
            color: $color-3;
        }
    }
}
.map {
    overflow: hidden;
    z-index: 1;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    position: relative;

    :deep(.leaflet-container) {
        .leaflet-control-attribution {
            display: none !important;
        }
        .leaflet-control-zoom {
            display: none;
        }
    }
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
}
</style>