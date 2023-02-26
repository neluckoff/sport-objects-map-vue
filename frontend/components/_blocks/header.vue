<template>
    <header>
        <div class="container">
            <div class="row">
                <div class="col-xxl-12">
                    <div class="header">
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
                </div>
            </div>
        </div>
    </header>
</template>

<style lang="scss" scoped>
    .header {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #f7f7f7;

        &__image {
            margin-right: 20px;

            .svg {
                width: 48px;
                height: auto;
                
                :deep() svg {
                    fill: #F34723;
                }
            }
        }

        &__text {
            &-basic {
                color: #212121;
                font-size: 22px;
            }

            &-red {
                font-size: 22px;
                color: #F34723;
            }
        }
    }
</style>