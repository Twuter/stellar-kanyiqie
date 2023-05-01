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
    def show(self):
        controls = self.Layout()
        self.doModal('main',800,600,'看一切',controls)
    def Layout(self):
        mediagrid_layout = [
            [
                {
                    'group': [
                        {'type':'image','name':'picture', '@click':'on_grid_click'},
                        {'type':'link','name':'title','textColor':'#ff7f00','fontSize':13,'height':0.15,'hAlign':'center','@click':'on_grid_click'}
                    ],
                    'dir':'vertical'
                }
            ]
        ]
        controls = [
            {'type':'space','height':5},
            {
                'group':[
                  {'type':'edit','name':'请输入内容','label':'搜索','width':300},
                  {'type':'button','name':'点击搜索','@click':''},#需要增加点击事件
            ]
            ,'dir':'horizontal'
            ,'height':30
                      },

            # {'type':'label','name':'搜索','height':5},
            {'type':'grid','name':'mediagrid','itemlayout':mediagrid_layout,'value':self.medias,'separator':True,'itemheight':200,'itemwidth':130},
            {'group':
                [
                    {'type':'space'},
                    {'group':
                        [
                            {'type':'label','name':'cur_page',':value':'cur_page'},
                            {'type':'link','name':'首页','fontSize':13,'@click':'onClickFirstPage'},
                            {'type':'link','name':'上一页','fontSize':13,'@click':'onClickFormerPage'},
                            {'type':'link','name':'下一页','fontSize':13,'@click':'onClickNextPage'},
                            {'type':'link','name':'末页','fontSize':13,'@click':'onClickLastPage'},
                            {'type':'label','name':'max_page',':value':'max_page'},
                        ]
                        ,'width':0.7
                    },
                    {'type':'space'}
                ]
                ,'height':30
            },
            {'type':'space','height':5}
        ]
        return controls




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
    plugin = KanyiqiePlugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

    """函数调用销毁函数
    参数     ----------
    plugin : StellarPlayer.IStellarPlayerPlugin
    IStellarPlayerPlugin实例对象
    返回：
        player
    """