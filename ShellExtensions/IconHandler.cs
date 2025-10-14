using SharpShell.SharpIconHandler;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ShellExtensions
{
    /// <summary>
    /// The DllIconHandler is a Shell Icon Handler exception that
    /// shows different icons for native and managed DLLs.
    /// </summary>
    public class IconHandler : SharpIconHandler
    {
        [ComVisible(true)]
        public class DllIconHandler : SharpIconHandler
    }
}
