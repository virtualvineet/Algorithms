#!/usr/bin/python

import os
import time
import sys

testcommand = {}
numtest = {}
#benchlist = {'catia-03','ensight-04','lightwave-01','maya-03','proe-05','sw-02','tcvis-02'}
#benchlist = {'tcvis-02'}
basedir = '/home/vineet/Benchmarks/'
benchdir = '/home/vineet/Benchmarks/SPECviewperf-11.0.0-Linux/viewsets/'
basecmd = '/home/vineet/Benchmarks/SPECviewperf-11.0.0-Linux/viewperf/viewperf11.0/viewperf/viewperf -versionpath ../../viewperf/viewperf11.0 -viewset '

numtest['catia-03'] = 7
numtest['ensight-04'] = 5
numtest['lightwave-01'] = 10
numtest['maya-03'] = 11 
numtest['proe-05'] = 6
numtest['sw-02'] = 10
numtest['tcvis-02'] = 5
numtest['snx-01'] = 13

testcommand['catia-03-0']="-reset" 
testcommand['catia-03-1']="-testnum 1 -weight 12.0 -mh Body_Wireframe_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -gr" 
testcommand['catia-03-2']="-testnum 2 -weight 12.0 -mh Body_Shading_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -gr -nt" 
testcommand['catia-03-3']="-testnum 3 -weight 14.0 -mh Body_ShadingEdges_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -gr -nt" 
testcommand['catia-03-4']="-testnum 4 -weight 14.0 -mh Body_Shading_AmbReflection -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -nt -traceClears -copyTexUseViewportSize -forceShadowTextureCreate" 
testcommand['catia-03-5']="-testnum 5 -weight 12.0 -mh Holland3MP_Wireframe_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -depthRange 1 -10000 -gr -nt" 
testcommand['catia-03-6']="-testnum 6 -weight 12.0 -mh Holland3MP_Shading_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -depthRange 1 -10000 -gr -nt" 
testcommand['catia-03-7']="-testnum 7 -weight 12.0 -mh Holland3MP_ShadingEdges_AmbOFF -zb -tracelights -mp 12 -clearcolor .2 .2 .2 1.0 -grab grab.scr -gather -useAlpha -wt -depthRange 1 -10000 -gr -nt" 
testcommand['catia-03-8']="-zb -generateScore -executebatch -useAlpha" 

testcommand['ensight-04-0']="-reset" 
testcommand['ensight-04-1']="-testnum 1 -weight 20.0 -mh wireframe -dl -zb -tracelights -mp 30 -grab grab.scr -gr -wtNewStyle" 
testcommand['ensight-04-2']="-testnum 2 -weight 20.0 -mh shaded -dl -zb -tracelights -mp 30 -grab grab.scr -ignorePolygonMode -gr -wtNewStyle" 
testcommand['ensight-04-3']="-testnum 3 -weight 20.0 -mh texture2 -dl -zb -tracelights -mp 30 -grab grab.scr -gr -wtNewStyle" 
testcommand['ensight-04-4']="-testnum 4 -weight 20.0 -mh texture -dl -zb -tracelights -mp 30 -grab grab.scr -gr -wtNewStyle" 
testcommand['ensight-04-5']="-testnum 5 -weight 20.0 -mh texturepeel -dl -zb -tracelights -mp 30 -grab grab.scr -wtNewStyle" 
testcommand['ensight-04-6']="-zb -generateScore" 

testcommand['lightwave-01-0']="-reset" 
testcommand['lightwave-01-1']=" -testnum 1 -weight 10.0 -mh buildingShaded -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -am -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -zx .5 -zy .5 -zz .5 -identityRotate" 
testcommand['lightwave-01-2']=" -testnum 2 -weight 10.0 -mh buildingTextured -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -am -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -zx .5 -zy .5 -zz .5 -identityRotate -nt" 
testcommand['lightwave-01-3']=" -testnum 3 -weight 10.0 -mh buildingTexturedTransparent -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -am -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -zx .5 -zy .5 -zz .5 -identityRotate -nt" 
testcommand['lightwave-01-4']=" -testnum 4 -weight 10.0 -mh buildingTextureWire -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -am -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -zx .5 -zy .5 -zz .5 -identityRotate -nt" 
testcommand['lightwave-01-5']=" -testnum 5 -weight 10.0 -mh buildingWire -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -am -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -zx .5 -zy .5 -zz .5 -identityRotate -nt" 
testcommand['lightwave-01-6']=" -testnum 6 -weight 10.0 -mh carTextured -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -zx 2 -zy 2 -zz 2 -useMultiTextureV -nt -wtNewStyle" 
testcommand['lightwave-01-7']=" -testnum 7 -weight 10.0 -mh carTexturedTransparent -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -zx 2 -zy 2 -zz 2 -useMultiTextureV -nt -wtNewStyle" 
testcommand['lightwave-01-8']=" -testnum 8 -weight 10.0 -mh matrixTextured -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -gr -zx 2 -zy 2 -zz 2 -nt" 
testcommand['lightwave-01-9']=" -testnum 9 -weight 10.0 -mh virusShaded -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -gr -zx 25 -zy 25 -zz 25 -nt" 
testcommand['lightwave-01-10']=" -testnum 10 -weight 10.0 -mh virusWire -zb -tracelights -mp 30 -clearcolor .3 .3 .3 1.0 -grab grab.scr -gather -gr -zx 25 -zy 25 -zz 25 -nt" 
testcommand['lightwave-01-11']="-zb -generateScore -executebatch" 

testcommand['maya-03-0']="-reset" 
testcommand['maya-03-1']="-testnum 1 -weight 9.0 -mh handShaded -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -allmatrix -forceModelViewMatrixRotate -gr" 
testcommand['maya-03-2']="-testnum 2 -weight 9.0 -mh handShadedHQ -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -allmatrix -forceModelViewMatrixRotate -gr -nt" 
testcommand['maya-03-3']="-testnum 3 -weight 9.0 -mh handWire -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -allmatrix -forceModelViewMatrixRotate -gr -nt" 
testcommand['maya-03-4']="-testnum 4 -weight 9.0 -mh squidShaded -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -zx 1.5 -zy 1.5 -zz 1.5 -nt" 
testcommand['maya-03-5']="-testnum 5 -weight 9.0 -mh squidShadedHQ -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -nt" 
testcommand['maya-03-6']="-testnum 6 -weight 10.0 -mh toyStoreShaded -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -wt -gr -depthRange 1 -10000 -nt" 
testcommand['maya-03-7']="-testnum 7 -weight 9.0 -mh toyStoreWire -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -wt -gr -depthRange 1 -10000 -nt" 
testcommand['maya-03-8']="-testnum 8 -weight 9.0 -mh wolfFurSelect -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -zx 2.5 -zy 2.5 -zz 2.5 -nt" 
testcommand['maya-03-9']="-testnum 9 -weight 9.0 -mh wolfFurSelectHQ -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -allmatrix -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -nt" 
testcommand['maya-03-10']="-testnum 10 -weight 9.0 -mh wolfShaded -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -ignorePreAttFog -zx 2 -zy 2 -zz 2 -nt" 
testcommand['maya-03-11']="-testnum 11 -weight 9.0 -mh wolfShadedHQ -zb -tracelights -mp 12 -clearcolor 0.2 .2 .2 1.0 -useDepthMask -grab grab.scr -gather -gr -allmatrix -forceProjectionMatrixRotate .5 -maxRotateAngle 5 -ignorePreAttFog -nt" 
testcommand['maya-03-12']="-zb -generateScore -executebatch" 

testcommand['proe-05-0']="-reset" 
testcommand['proe-05-1']="-testnum 1 -weight 17  -mh wireCar -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -wt -gr" 
testcommand['proe-05-2']="-testnum 2 -weight 17  -mh shadedCar -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -nt -wt -gr" 
testcommand['proe-05-3']="-testnum 3 -weight 17  -mh shadedCarEdges -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -nt -wt -gr" 
testcommand['proe-05-4']="-testnum 4 -weight 17  -mh shadedCarEnv -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -nt" 
testcommand['proe-05-5']="-testnum 5 -weight 17  -mh shadedPart -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -nt  -gr -wt" 
testcommand['proe-05-6']="-testnum 6 -weight 15  -mh shadedPartMirror -tracelights -grab grab.scr -zb -useDepthFunc 515  -mp 12 -gather -nt -zx 8 -zy 8 -zz 8" 
testcommand['proe-05-7']="-zb -generateScore -executebatch" 
					
testcommand['sw-02-0']="-reset" 
testcommand['sw-02-1']="-testnum 1  -weight 10  -mh toyCarWire -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -gr" 
testcommand['sw-02-2']="-testnum 2  -weight 10  -mh toyCarHLR -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-3']="-testnum 3  -weight 10  -mh toyCarShaded -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-4']="-testnum 4  -weight 10  -mh toyCarShadedEdges -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-5']="-testnum 5  -weight 10  -mh toyCarRealView -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-6']="-testnum 6  -weight 10  -mh engineWire -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-7']="-testnum 7  -weight 10  -mh engineHLR -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-8']="-testnum 8  -weight 10  -mh engineShaded -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-9']="-testnum 9  -weight 10  -mh engineShadedEdges -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-10']="-testnum 10 -weight 10  -mh engineRealView -forceWindowOrtho  -projectionRotate 45 100 100 100 -clearcolor .3 .3 .3 1 -zb -allmatrix -tracelights -useDepthMask -mp 12 -grab grab.scr -gather -nt -gr" 
testcommand['sw-02-11']="-zb -generateScore -executebatch" 

testcommand['tcvis-02-0']="-reset" 
testcommand['tcvis-02-1']="-testnum 1 -weight 20 -gr -mh viewset1 -gather -tracelights -zb -mp 12 -grab grab.scr -clearcolor .3 .3 .3 1.0 -allmatrix -forceModelViewMatrixRotate -maxRotateAngle 45" 
testcommand['tcvis-02-2']="-testnum 2 -weight 20 -gr -mh viewset2 -gather -tracelights -zb -mp 12 -grab grab.scr -clearcolor .3 .3 .3 1.0 -allmatrix -forceModelViewMatrixRotate -maxRotateAngle 45 -nt" 
testcommand['tcvis-02-3']="-testnum 3 -weight 20 -gr -mh viewset3 -gather -tracelights -zb -mp 12 -grab grab.scr -clearcolor .3 .3 .3 1.0 -allmatrix -forceModelViewMatrixRotate -maxRotateAngle 45 -nt" 
testcommand['tcvis-02-4']="-testnum 4 -weight 20 -gr -mh viewset4 -gather -tracelights -zb -mp 12 -grab grab.scr -clearcolor .3 .3 .3 1.0 -allmatrix -forceModelViewMatrixRotate -maxRotateAngle 45 -nt" 
testcommand['tcvis-02-5']="-testnum 5 -weight 20 -gr -mh viewset5 -gather -tracelights -zb -mp 12 -grab grab.scr -clearcolor .3 .3 .3 1.0 -allmatrix -forceModelViewMatrixRotate -maxRotateAngle 45 -nt" 
testcommand['tcvis-02-6']="-zb -generateScore -executebatch" 
					 
testcommand['snx-01-0']="-reset" 
testcommand['snx-01-1']="-testnum 1 -weight 10.0 -mh BPLshaded -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 1 -alternatePackFile 1" 
testcommand['snx-01-2']="-testnum 2 -weight 10.0 -mh BPLshaded_edges -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 1 -alternatePackFile 1" 
testcommand['snx-01-3']="-testnum 3 -weight 7.0 -mh BPLwireframe -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 1 -alternatePackFile 1" 
testcommand['snx-01-4']="-testnum 4 -weight 7.0 -mh BPLwireframe_aa -dl -ls -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 1 -alternatePackFile 1" 
testcommand['snx-01-5']="-testnum 5 -weight 6.0 -mh BPLwireframe_dim_edges -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -traceClears -alternateShareFile 1 -alternatePackFile 1" 
testcommand['snx-01-6']="-testnum 6 -weight 10.0 -mh TLECTWshaded -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 2 -alternatePackFile 2" 
testcommand['snx-01-7']="-testnum 7 -weight 10.0 -mh TLECTWshaded_edges_aa -dl -ls -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr -alternateShareFile 2 -alternatePackFile 2" 
testcommand['snx-01-8']="-testnum 8 -weight 5.0 -mh TLECTWwireframe_dim_edges_aa -dl -ls -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -traceClears -alternateShareFile 2 -alternatePackFile 2" 
testcommand['snx-01-9']="-testnum 9 -weight 5.0 -mh TLECTWwireframe_hidden_edges_aa -dl -ls -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -traceClears -alternateShareFile 2 -alternatePackFile 2" 
testcommand['snx-01-10']="-testnum 10 -weight 10.0 -mh TLMEshaded -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr" 
testcommand['snx-01-11']="-testnum 11 -weight 10.0 -mh TLMEshaded_edges -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -gr" 
testcommand['snx-01-12']="-testnum 12 -weight 5.0 -mh TLMEwireframe_dim_edges -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -traceClears" 
testcommand['snx-01-13']="-testnum 13 -weight 5.0 -mh TLMEwireframe_hidden_edges -dl -zb -tracelights -mp 30 -ugsMatrix -useStencil -useDepthMask -traceDepthFunc -grab grab.scr -wtNewStyle -traceClears" 
testcommand['snx-01-14']="-zb -generateScore" 

bench = sys.argv[1]
#cpus = sys.argv[2]
cpus = 2
#cpuconfig = sys.argv[3]
cpuconfig = "het"
#freq = sys.argv[4]
freq = 255

print bench
#os.system('cat /proc/hetero_events 1> '+basedir + bench +'-'+str(cpus)+'-'+str(cpuconfig)+'-'+str(freq)+'-monitor.out &');
os.chdir(benchdir+bench)
for i in range(numtest[bench]+2):
	os.system(basecmd+bench+ " "+ testcommand[bench+'-'+str(i)])
#os.chdir(basedir)
#os.system('sudo pkill cat')
#os.system('mv /home/vishal/benchmarks/SPECviewperf-11.0.0-Linux/viewsets/'+bench+'/'+bench+'-'+str(cpus)+'-'+str(run)+'-time.out .' )
os.system('cp /home/vineet/Benchmarks/SPECviewperf-11.0.0-Linux/viewperf/viewperf11.0/results/'+bench+'/viewperfresult.txt ./'+bench+'-'+str(cpus)+'-'+str(cpuconfig)+'-'+str(freq)+'-fps.out')
