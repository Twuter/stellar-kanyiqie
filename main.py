# -*- coding: utf-8 -*-
import StellarPlayer


class KanyiqiePlugin(StellarPlayer.IStellarPlayerPlugin):
    def __init__(self, player: StellarPlayer.IStellarPlayer):
        super().__init__(player)
        self.configjson = ''
        self.medias = []
        self.pageindex = 0
        self.pagenumbers = 0
        self.cur_page = ''
        self.max_page = ''
        self.pg = ''
        self.wd = ''
        self.source = []
        self.allmovidesdata = {}
        self.mediasize = 18

    def handleRequest(self, method, args):
        if hasattr(self.simple, f"on_{method}"):
            getattr(self.simple, f"on_{method}")(args)

    def start(self):
        super().start()
        print("插件启动")

    def stop(self):
        super().stop()
        print("插件停止")

    def newPlugin(player: StellarPlayer.IStellarPlayer, *arg):
        print("插件初始化")
        return Plugin(player)
