#!/usr/bin/env python

def plot( plt, params ):

    #-:     lines linking points (default)
    #--:    lines linking points (default)
    #o:     circles, no lines linking points

    fig, axs = plt.subplots(2,2)
    axs[0,0].plot([0,1], linestyle='-')
    axs[0,0].set_title('-')
    axs[0,1].plot([0,1], linestyle='o')
    axs[0,1].set_title('o')
    axs[1,0].plot([0,1], linestyle='--')
    axs[1,0].set_title('- -')
    #BUG svg output cannot contain -- because it messes up a comment =)
    #but reporte solution merged already for next release.
