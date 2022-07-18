# Wavelet Tree
Simple implementation of Wavelet Tree with access, rank, select operations. The Wavelet Tree is a type of Succinct data structure which enables $O(log(\sigma))$ time complexity over `rank, select, access` operations. 

## BitVector Class
Simplified implementation with no regards to time complexity.

## WaveletNode Class
Node class for the Wavelet Tree, includes `Bit Vector, parent, left, right, sign and label`.

## WaveletTree Class
Main class for Wavelet Tree construction, has `build_tree` method for building a Wavelet Tree over the defined text.