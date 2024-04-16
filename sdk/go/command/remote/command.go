// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package remote

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-command/sdk/go/command/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A command to run on a remote host.
// The connection is established via ssh.
type Command struct {
	pulumi.CustomResourceState

	// The parameters with which to connect to the remote host.
	Connection ConnectionOutput `pulumi:"connection"`
	// The command to run on create.
	Create pulumi.StringPtrOutput `pulumi:"create"`
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete pulumi.StringPtrOutput `pulumi:"delete"`
	// Additional environment variables available to the command's process.
	// Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
	// Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
	// with the variables in the form 'VAR=value command'.
	Environment pulumi.StringMapOutput `pulumi:"environment"`
	// If the command's stdout and stderr should be logged.
	LogOutput pulumi.BoolPtrOutput `pulumi:"logOutput"`
	// The standard error of the command's process
	Stderr pulumi.StringOutput `pulumi:"stderr"`
	// Pass a string to the command's process as standard in
	Stdin pulumi.StringPtrOutput `pulumi:"stdin"`
	// The standard output of the command's process
	Stdout pulumi.StringOutput `pulumi:"stdout"`
	// Trigger replacements on changes to this input.
	Triggers pulumi.ArrayOutput `pulumi:"triggers"`
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update pulumi.StringPtrOutput `pulumi:"update"`
}

// NewCommand registers a new resource with the given unique name, arguments, and options.
func NewCommand(ctx *pulumi.Context,
	name string, args *CommandArgs, opts ...pulumi.ResourceOption) (*Command, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Connection == nil {
		return nil, errors.New("invalid value for required argument 'Connection'")
	}
	args.Connection = args.Connection.ToConnectionOutput().ApplyT(func(v Connection) Connection { return *v.Defaults() }).(ConnectionOutput)
	if args.LogOutput == nil {
		args.LogOutput = pulumi.BoolPtr(true)
	}
	if args.Connection != nil {
		args.Connection = pulumi.ToSecret(args.Connection).(ConnectionInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"connection",
	})
	opts = append(opts, secrets)
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"triggers[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Command
	err := ctx.RegisterResource("command:remote:Command", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCommand gets an existing Command resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCommand(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CommandState, opts ...pulumi.ResourceOption) (*Command, error) {
	var resource Command
	err := ctx.ReadResource("command:remote:Command", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Command resources.
type commandState struct {
}

type CommandState struct {
}

func (CommandState) ElementType() reflect.Type {
	return reflect.TypeOf((*commandState)(nil)).Elem()
}

type commandArgs struct {
	// The parameters with which to connect to the remote host.
	Connection Connection `pulumi:"connection"`
	// The command to run on create.
	Create *string `pulumi:"create"`
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete *string `pulumi:"delete"`
	// Additional environment variables available to the command's process.
	// Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
	// Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
	// with the variables in the form 'VAR=value command'.
	Environment map[string]string `pulumi:"environment"`
	// If the command's stdout and stderr should be logged.
	LogOutput *bool `pulumi:"logOutput"`
	// Pass a string to the command's process as standard in
	Stdin *string `pulumi:"stdin"`
	// Trigger replacements on changes to this input.
	Triggers []interface{} `pulumi:"triggers"`
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update *string `pulumi:"update"`
}

// The set of arguments for constructing a Command resource.
type CommandArgs struct {
	// The parameters with which to connect to the remote host.
	Connection ConnectionInput
	// The command to run on create.
	Create pulumi.StringPtrInput
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete pulumi.StringPtrInput
	// Additional environment variables available to the command's process.
	// Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
	// Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
	// with the variables in the form 'VAR=value command'.
	Environment pulumi.StringMapInput
	// If the command's stdout and stderr should be logged.
	LogOutput pulumi.BoolPtrInput
	// Pass a string to the command's process as standard in
	Stdin pulumi.StringPtrInput
	// Trigger replacements on changes to this input.
	Triggers pulumi.ArrayInput
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update pulumi.StringPtrInput
}

func (CommandArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*commandArgs)(nil)).Elem()
}

type CommandInput interface {
	pulumi.Input

	ToCommandOutput() CommandOutput
	ToCommandOutputWithContext(ctx context.Context) CommandOutput
}

func (*Command) ElementType() reflect.Type {
	return reflect.TypeOf((**Command)(nil)).Elem()
}

func (i *Command) ToCommandOutput() CommandOutput {
	return i.ToCommandOutputWithContext(context.Background())
}

func (i *Command) ToCommandOutputWithContext(ctx context.Context) CommandOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CommandOutput)
}

// CommandArrayInput is an input type that accepts CommandArray and CommandArrayOutput values.
// You can construct a concrete instance of `CommandArrayInput` via:
//
//	CommandArray{ CommandArgs{...} }
type CommandArrayInput interface {
	pulumi.Input

	ToCommandArrayOutput() CommandArrayOutput
	ToCommandArrayOutputWithContext(context.Context) CommandArrayOutput
}

type CommandArray []CommandInput

func (CommandArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Command)(nil)).Elem()
}

func (i CommandArray) ToCommandArrayOutput() CommandArrayOutput {
	return i.ToCommandArrayOutputWithContext(context.Background())
}

func (i CommandArray) ToCommandArrayOutputWithContext(ctx context.Context) CommandArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CommandArrayOutput)
}

// CommandMapInput is an input type that accepts CommandMap and CommandMapOutput values.
// You can construct a concrete instance of `CommandMapInput` via:
//
//	CommandMap{ "key": CommandArgs{...} }
type CommandMapInput interface {
	pulumi.Input

	ToCommandMapOutput() CommandMapOutput
	ToCommandMapOutputWithContext(context.Context) CommandMapOutput
}

type CommandMap map[string]CommandInput

func (CommandMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Command)(nil)).Elem()
}

func (i CommandMap) ToCommandMapOutput() CommandMapOutput {
	return i.ToCommandMapOutputWithContext(context.Background())
}

func (i CommandMap) ToCommandMapOutputWithContext(ctx context.Context) CommandMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CommandMapOutput)
}

type CommandOutput struct{ *pulumi.OutputState }

func (CommandOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Command)(nil)).Elem()
}

func (o CommandOutput) ToCommandOutput() CommandOutput {
	return o
}

func (o CommandOutput) ToCommandOutputWithContext(ctx context.Context) CommandOutput {
	return o
}

// The parameters with which to connect to the remote host.
func (o CommandOutput) Connection() ConnectionOutput {
	return o.ApplyT(func(v *Command) ConnectionOutput { return v.Connection }).(ConnectionOutput)
}

// The command to run on create.
func (o CommandOutput) Create() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Command) pulumi.StringPtrOutput { return v.Create }).(pulumi.StringPtrOutput)
}

// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
// Command resource from previous create or update steps.
func (o CommandOutput) Delete() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Command) pulumi.StringPtrOutput { return v.Delete }).(pulumi.StringPtrOutput)
}

// Additional environment variables available to the command's process.
// Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
// Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
// with the variables in the form 'VAR=value command'.
func (o CommandOutput) Environment() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Command) pulumi.StringMapOutput { return v.Environment }).(pulumi.StringMapOutput)
}

// If the command's stdout and stderr should be logged.
func (o CommandOutput) LogOutput() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Command) pulumi.BoolPtrOutput { return v.LogOutput }).(pulumi.BoolPtrOutput)
}

// The standard error of the command's process
func (o CommandOutput) Stderr() pulumi.StringOutput {
	return o.ApplyT(func(v *Command) pulumi.StringOutput { return v.Stderr }).(pulumi.StringOutput)
}

// Pass a string to the command's process as standard in
func (o CommandOutput) Stdin() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Command) pulumi.StringPtrOutput { return v.Stdin }).(pulumi.StringPtrOutput)
}

// The standard output of the command's process
func (o CommandOutput) Stdout() pulumi.StringOutput {
	return o.ApplyT(func(v *Command) pulumi.StringOutput { return v.Stdout }).(pulumi.StringOutput)
}

// Trigger replacements on changes to this input.
func (o CommandOutput) Triggers() pulumi.ArrayOutput {
	return o.ApplyT(func(v *Command) pulumi.ArrayOutput { return v.Triggers }).(pulumi.ArrayOutput)
}

// The command to run on update, if empty, create will
// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
// are set to the stdout and stderr properties of the Command resource from previous
// create or update steps.
func (o CommandOutput) Update() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Command) pulumi.StringPtrOutput { return v.Update }).(pulumi.StringPtrOutput)
}

type CommandArrayOutput struct{ *pulumi.OutputState }

func (CommandArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Command)(nil)).Elem()
}

func (o CommandArrayOutput) ToCommandArrayOutput() CommandArrayOutput {
	return o
}

func (o CommandArrayOutput) ToCommandArrayOutputWithContext(ctx context.Context) CommandArrayOutput {
	return o
}

func (o CommandArrayOutput) Index(i pulumi.IntInput) CommandOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Command {
		return vs[0].([]*Command)[vs[1].(int)]
	}).(CommandOutput)
}

type CommandMapOutput struct{ *pulumi.OutputState }

func (CommandMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Command)(nil)).Elem()
}

func (o CommandMapOutput) ToCommandMapOutput() CommandMapOutput {
	return o
}

func (o CommandMapOutput) ToCommandMapOutputWithContext(ctx context.Context) CommandMapOutput {
	return o
}

func (o CommandMapOutput) MapIndex(k pulumi.StringInput) CommandOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Command {
		return vs[0].(map[string]*Command)[vs[1].(string)]
	}).(CommandOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CommandInput)(nil)).Elem(), &Command{})
	pulumi.RegisterInputType(reflect.TypeOf((*CommandArrayInput)(nil)).Elem(), CommandArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CommandMapInput)(nil)).Elem(), CommandMap{})
	pulumi.RegisterOutputType(CommandOutput{})
	pulumi.RegisterOutputType(CommandArrayOutput{})
	pulumi.RegisterOutputType(CommandMapOutput{})
}
