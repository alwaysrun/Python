# -*- coding: utf-8 -*-
'''
Bi-Tree: order-tree
'''

class BiNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class BiTree:
    def __init__(self):
        self.root = None
    
    def AddNode(self, node:BiNode)->BiNode:
        if not self.root:
            self.root = node
            return node
        
        # travel in layer, and build a balance-bi-tree
#        layer = []
#        layer.append(self.root)
#        while True:
#            cur = layer.pop(0)  # get the first
#            if not cur.left:
#                cur.left = node
#                break
#            elif not cur.right:
#                cur.right = node
#                break
#            else:   # has both children, check next
#                layer.append(cur.left)
#                layer.append(cur.right)
        
        # insert as ordered-tree
        cur = self.root
        last = None
        while cur:
            last = cur
            if cur.data>node.data:
                cur = cur.left
            else:
                cur = cur.right
        if last.data>node.data:
            last.left = node
        else:
            last.right = node
            
        return node
    
    def AddData(self, data)->BiNode:
        node = BiNode(data)
        return self.AddNode(node)
    
    def Output(self):
        if not self.root:
            print('[None]')
            return
        
        diff = 2
        strOut = []
#        def layerPrint(nd, ind, layer):
#            if not nd: return
#            if len(strOut) <= layer:
#                strOut.append('')
#            strOut[layer] += '{0}{1}'.format(' '*3, nd.data)
#            
#            layer+=1
#            layerPrint(nd.left, ind-diff, layer)
#            layerPrint(nd.right, ind+diff, layer)
#        layerPrint(self.root, 20, 0)      

        class outLayer:
            def __init__(self, node, layer, indent=0):
                self.node = node
                self.layer = layer
                self.indent = int(indent)
                
        maxlay = self.LayerAndWidth()[0]
        layers = []
        out = []
        layers.append(outLayer(self.root, 1, maxlay*diff+20))
        while layers:
            ly = layers.pop(0)
            out.append(ly)
            
            indiff = (maxlay-ly.layer+1)*diff/2
            if ly.node.left:
                layers.append(outLayer(ly.node.left, ly.layer+1, ly.indent-indiff-1)) 
            if ly.node.right:
                layers.append(outLayer(ly.node.right, ly.layer+1, ly.indent+indiff+1)) 
       
        last = 0
        leftindent = 0
        for ly in out:
            if last != ly.layer:    # the most-left node
                leftindent = indent = ly.indent
                last = ly.layer
                strOut.append('')  
            else:
                indent = int(ly.indent - leftindent) 
                leftindent = ly.indent
            
            if indent<1: indent = 1
            strOut[last-1] += '{0}{1}'.format(' '*indent, ly.node.data) 

        for str in strOut:
            print(str)   
        
    def LayerWalk(self)->list:
        if not self.root:
            return []
        
        layer = []
        requ = []
        layer.append(self.root)
        while layer:    # not empty
            cur = layer.pop(0)
            requ.append(cur)
            if cur.left:
                layer.append(cur.left)
            if cur.right:
                layer.append(cur.right)
             
        # all nodes in requ
        return requ;
        
    def InoderWalk(self)->list:
        if not self.root:
            return []
                
        requ = []
        # recursion mode
        def inorderRec(nd):
            if not nd: return
            inorderRec(nd.left)
            requ.append(nd)
            inorderRec(nd.right)
        # end-rec
        inorderRec(self.root)
        
        return requ
    
    def PreorderWalk(self)->list:
        if not self.root:
            return []
        
        requ = []
        #recursion mode
        def preoderRec(nd):
            if not nd: return
            requ.append(nd)
            preoderRec(nd.left)
            preoderRec(nd.right)
        #end-rec
        preoderRec(self.root)
        
        return requ;
    
    def PostorderWalk(self)->list:
        if not self.root:
            return []
        
        requ = []
        #recursion mode
        def postorderRec(nd):
            if not nd: return
            postorderRec(nd.left)
            postorderRec(nd.right)
            requ.append(nd)
        #end-rec
        postorderRec(self.root)
        
        return requ;
        
    
    class nodeLayer:
        def __init__(self, nd:BiNode, layer:int):
            self.node = nd
            self.layer = layer
            
    def getLayers(self)->list:
        if not self.root:
            return []
        
        layer = []
        req = []
        req.append(self.nodeLayer(self.root, 1))
        while req:
            cur = req.pop(0)
            layer.append(cur)
            if cur.node.left:
                req.append(self.nodeLayer(cur.node.left, cur.layer+1))
            if cur.node.right:
                req.append(self.nodeLayer(cur.node.right, cur.layer+1))
#        def loopLayer(nd, ind):
#            if not nd: return
#            layer.append(self.nodeLayer(nd, ind))
#            ind += 1
#            loopLayer(nd.left, ind)
#            loopLayer(nd.right, ind)
            
        # all get
#        loopLayer(self.root, 1)
        
        return layer
    
    def LayerAndWidth(self): # (maxLayer, (maxwidth-layer, maxwidth))
        from collections import Counter
        if not self.root:
            return (0, (0,0))
        
        layer = self.getLayers()
#        maxlayer = layer[len(layer)-1].layer
        maxlayer = max((x.layer for x in layer))
#        print( tuple('{0}:{1}'.format(x.node.data, x.layer) for x in layer) )
        widths = Counter((x.layer for x in layer))
#        print(maxlayer, widths)
#        print(widths.most_common(1)[0][1])
        return (maxlayer, widths.most_common(1)[0])
            
    
if __name__ == '__main__':
    import random
    import Test_data as td
    bt = BiTree()
    sqdata = []
    for _ in range(20):
        ele = random.randint(1, 99)
        sqdata.append(bt.AddData(ele))
        
#    td.PrintList(sqdata)
    print(bt.LayerAndWidth())
    bt.Output()
    td.PrintList(bt.LayerWalk())
    td.PrintList(bt.InoderWalk())
    td.PrintList(bt.PreorderWalk())
    td.PrintList(bt.PostorderWalk())
    