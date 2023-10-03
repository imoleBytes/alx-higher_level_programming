#include "lists.h"

/**
* insert_node - function to Inserts a number into a sorted singly-linked list.
* @head: A pointer to the head of the linked list.
* @number: number to insert.
* Return: NULL, if fails
*         Otherwise - a pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	(*new).n = number;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && (*temp).next->n < number)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (new);
}
