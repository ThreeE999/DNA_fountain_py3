# encoding: utf-8
if __name__ == '__main__':
    from encode import Encode
    from decode import Decode
    from time import sleep
    start = 'tree.png'
    dna = 'tree.tar.gz.dna'
    final = 'tree.tar.gz.final     '
    print('encoding................')
    sleep(0.5)
    Encode(file_in=start,out=dna,
           size=32,rs=2,max_homopolymer=3,gc=0.05,delta=0.001,c_dist=0.025,stop=2000,no_fasta=True).main()
    print('decoding................')
    sleep(0.5)
    chunk = int(input('please input the number of chunk or segments:'))
    Decode(file_in = dna, out = final,
           header_size = 4, rs = 2, delta = 0.001, c_dist = 0.025, chunk_num = chunk, max_homopolymer = 3, gc = 0.05, max_hamming = 0).main()
    print('complete!')
    print('start file:', start ,'\ndna file:', dna ,'\nrecover file:', final)