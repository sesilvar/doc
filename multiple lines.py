def read_all_molecules(r):
    '''Read zero or more molecules from reader r , returning a list of the molecules read.'''

    result = []
    line = r.readline()
    while line:

        molecule , line = read_molecules(r , line)
        result.append(molecule)
    return result

def read_molecule(r,line):
    '''Read a molecule from reader r . The variable 'line' is the first line of the molecule to be read ;
    the result is the molecule , and the first line after it (or the empty string if the end of file has been reached).'''

    fields = line.split()
    molecule = [fields[1]]
    line = r.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split()
        key , num , type , x , y , z , = fields
        molecule.append((type , x , y , z))
        line = r.readline()
    return molecule , line

# 两层函数嵌套，下一行为 COMPND 则执行新的 read_molecule ，空行则函数停止，返回 result