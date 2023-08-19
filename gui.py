import asyncio
import json
from enum import Enum
import streamlit as st
from core.tg_api_connector import Broadcaster

col1, col2 = st.columns(2)


class Protocols(Enum):
    HTTP = 'http'
    HTTPS = 'https'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'


protocol_options = [protocol.value for protocol in Protocols]

with col1:
    phone = st.text_input(label='Введите номер телфона')
    st.write('Введите данные прокси')
    proxy = st.data_editor(
        {
            ('протокол',): st.selectbox('Выберите протокол', protocol_options),
            ('ip',): '',
            ('порт',): '',
            ('логин',): '',
            ('пароль',): ''
        },
        column_config={0: 'параметры', 1: 'значения'},
        use_container_width=True
    )
    if phone and '' not in proxy.values():
        if st.button(label='Отправить код подтверждения'):
            b = Broadcaster(phone, proxy)
            asyncio.run(b.log_in())
            code = st.text_input(label='Введите код подтверждения')
            with open('code_proxy.json', 'r') as file:
                data = json.load(file)
                data.update({phone: code})
            with open('code_proxy.json', 'w') as file:
                json.dump(data, file)
            if st.button(label='Посмотреть аккаунт'):
                me = asyncio.run(b.show_me())
                st.write(me)

with col2:
    st.write('Прокси можно приобрести например здесь: https://proxy-seller.io/')
    st.write('В результате покупки Вы получите письмо с необходимыми данными.\n\n'
             'Вы можете использовать любой доступный проткол. Для целей рассылки принципиальной разницы нет.')
