<template>
    <div class="information" v-if="cardItem!=null">
        <div class="information__head">
            <h4>{{ cardItem.name }}</h4>
            <span>{{ cardItem.objectType }}</span>
            <div class="menu">
                <span class="menu__button" :class="{active: this.menu.desc === true}" @click="setDesc()">Описание</span>
                <span class="menu__button" :class="{active: this.menu.graph === true}" @click="setGraph()">График</span>
                <span class="menu__button" :class="{active: this.menu.contact === true}" @click="setContact()">Контакты</span>
            </div>
        </div>
        <div class="information__text" v-if="this.menu.desc === true">
            <div class="information__text-block description">
                <div class="info">
                    <span class="head-span">Информация</span>
                </div>
                <span class="desc">{{ cardItem.desc ? cardItem.desc : 'Информация отсутствует' }}</span>
            </div>
            <div class="information__text-block" v-if="cardItem.sportType != null">
                <div class="icon">
                    <base-svg name="volleyball"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Виды спорта</span>
                    <span class="info-span">{{ cardItem.sportType }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.active != null">
                <div class="icon">
                    <base-svg name="wave-pulse"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Статус объекта</span>
                    <span class="info-span">{{ cardItem.active == 'Y' ? 'Активный' : 'Неактивный' }} - {{ cardItem.action }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.oktmo != null">
                <div class="icon">
                    <base-svg name="book"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Код ОКТМО</span>
                    <span class="info-span">{{ cardItem.oktmo }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.fcp != null">
                <div class="icon">
                    <base-svg name="passport"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">ФСП</span>
                    <span class="info-span">{{ cardItem.fcp }}</span>
                </div>
            </div>
        </div>
        <div class="information__text" v-if="this.menu.graph === true">  
            <div class="information__text-block description" v-if="showGraph">
                <div class="info">
                    <span class="head-span">График финансирования</span>
                </div>
                <blocks-pie-finance :idObject="cardItem.id" ref="graph"></blocks-pie-finance>
            </div>
        </div>
        <div class="information__text" v-if="this.menu.contact === true">
            <div class="information__text-block" v-if="cardItem.address != null">
                <div class="icon">
                    <base-svg name="geo" class="geo-svg"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Адресс</span>
                    <span class="info-span">{{ cardItem.address }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.workingTime != null">
                <div class="icon">
                    <base-svg name="timer"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Рабочее время</span>
                    <span class="info-span">{{ cardItem.workingTime }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.phone != null">
                <div class="icon">
                    <base-svg name="phone"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Телефон</span>
                    <span class="info-span"><a :href="`tel:${cardItem.phone}`">{{ cardItem.phone }}</a></span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.url != null">
                <div class="icon">
                    <base-svg name="globe"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Ссылка на сайт</span>
                    <span class="info-span"><a :href="`${cardItem.url}`" target="_blank">{{ cardItem.url }}</a></span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        cardItem: {
            type: Object,
            default: null,
        },
        showGraph: {
            type: Boolean,
            default: true,
        },
        center: {
            type: Array,
            default: null,
        }
    },
    data: () => ({
        menu: {
            desc: true,
            graph: false,
            contact: false,
        }
    }),
    methods: {
        setDesc() {
            this.menu = {
                desc: true,
                graph: false,
                contact: false,
            }
        },
        setGraph() {
            this.menu = {
                desc: false,
                graph: true,
                contact: false,
            }
        },
        setContact() {
            this.menu = {
                desc: false,
                graph: false,
                contact: true,
            }
        },
    }
}
</script>

<style lang="scss" scoped>
.menu {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 20px;

    &__button {
        padding: 10px 20px;
        border-bottom: 3px solid $color-7;
        transition: all 0.8s ease;
        border-radius: 10px 10px 0 0;
        font-weight: 500;
        color: $color-7;
        cursor: pointer;

        &:hover {
            // background-color: $color-4;
            // border-radius: 8px;
            border-bottom: 3px solid $color-8;
        }
    }

    .active {
        border-bottom: 3px solid $color-3;
        // color: $color-3;
    }
}
.desc {
    color: #212121;
    line-height: 20px;
}
.information {
    padding: 20px;
    transition: all 5s ease;

    &__head {
        display: flex;
        flex-direction: column;
    }

    &__text {
        // padding-top: 10px;
        display: flex;
        flex-direction: column;

        &-block {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #f7f7f7;

            &:hover {
                .info {
                    .head-span {
                        color: $color-3;
                    }
                }
                .icon {
                    .svg {
                        :deep() svg {
                            fill: $color-3;
                        }
                    }
                }
            }

            .icon {
                margin-right: 20px;

                .svg {
                    width: 32px;
                    height: auto;

                    :deep() svg {
                        transition: all .2s ease-out;
                        fill: $color-5;
                        max-width: 100%;
                        max-height: 100%;
                    }
                }

                .geo-svg {
                    width: 28px;
                }
            }

            .info {
                display: flex;
                flex-direction: column;

                .head-span {                    
                    transition: all .2s ease-out;
                    font-weight: 600;
                    color: #212121;
                    font-size: 17px;
                    padding-bottom: 5px;
                }

                .info-span {
                    font-weight: 400;
                    color: #808080;
                    font-size: 17px;
                    padding-bottom: 0;

                    a {
                        font-weight: 400;
                        color: #808080;
                        font-size: 17px;
                        padding-bottom: 0;
                    }
                }
            }
        }

        .description {
            flex-direction: column;
            align-items: flex-start;
        }

        .graphic {
            flex-direction: column;
            
        }
    }

    h4 {
        font-size: 26px;
        padding-bottom: 5px;
        color: #212121;
    }
    span {
        font-size: 17px;
        color: #808080;
        padding-bottom: 10px;
    }
}
</style>