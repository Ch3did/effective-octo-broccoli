class XpathNotations:
    @classmethod
    def get_cookie_btn(self) -> str:
        return '//*[@id="site-content"]/div[2]/div[2]/div/div[2]/button[1]'

    @classmethod
    def get_date_btn(self) -> str:
        return (
            '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/button'
        )

    @classmethod
    def get_btn_year(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/ul/li[5]/button'

    @classmethod
    def get_btn_section(self):
        return (
            '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button'
        )

    @classmethod
    def get_section_list(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li'

    @classmethod
    def get_section(self, index):
        return f'//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li[{index}]/label'

    @classmethod
    def get_search_field(self):
        return '//*[@id="searchTextField"]'

    @classmethod
    def get_sort(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[1]/form/div[2]/div/select/option[2]'

    @classmethod
    def get_search_btn(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[1]/form/div[1]/button/svg'

    @classmethod
    def get_all_in_page(self):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[2]/ol/li'

    @classmethod
    def get_title(self, item):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[2]/ol/li[{item}]/div/div/div/a/h4'

    @classmethod
    def get_date(self, item):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[2]/ol/li[{item}]/div/span'

    @classmethod
    def get_description(self, item):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[2]/ol/li[{item}]/div/div/div/a/p[1]'

    @classmethod
    def get_picture_name(self, item):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[2]/ol/li[{item}]/div/div/figure/div/img'

    @classmethod
    def btn_show_more(self):
        return f'//*[@id="site-content"]/div[1]/div[2]/div[3]/div/button'
